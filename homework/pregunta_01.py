# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    import glob
    import os
    import pandas as pd

    def load_input(input_directory):
        files = glob.glob(f"{input_directory}/*/*")
        dataframes = []
    
        for file in files:
            target = os.path.basename(os.path.dirname(file))
            
            df_temp = pd.read_csv(
                file,
                header=None,
                delimiter="\t",
                names=["phrase"],
                index_col=None,
            )
            
            df_temp["target"] = target
            
            dataframes.append(df_temp)

        dataframe = pd.concat(dataframes, ignore_index=True)

        return dataframe
    
    def save_output(dataframe, output_directory, nombre):
        os.makedirs(output_directory, exist_ok=True)

        target_file = os.path.join(output_directory, nombre)

        if os.path.exists(target_file):
            os.remove(target_file)

        dataframe.to_csv(
            target_file,
            sep=",",
            index=False,
        )

    df_train = load_input("files/input/train")
    df_test = load_input("files/input/test")

    carpeta_destino = "files/output"

    save_output(df_train, carpeta_destino, "train_dataset.csv")
    save_output(df_test, carpeta_destino, "test_dataset.csv")

pregunta_01()