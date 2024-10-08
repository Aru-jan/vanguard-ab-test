def rename_columns(dataFrames, config):
    for name, dataFrame in dataFrames.items():
        new_names = {values['original_name']: new_name for new_name,
                     values in config['tables'][name]['columns'].items()}

        dataFrames[name] = dataFrame.rename(columns=new_names)
    return dataFrames

# select columns
def select_columns(dataFrames, config):
    for name, dataFrame in dataFrames.items():
        selected_columns = config['tables'][name]['columns'].keys()
        dataFrames[name] = dataFrame[selected_columns]
    return dataFrames

