def rename_columns(dataFrames, config):
    for name, dataFrame in dataFrames.items():
        new_names = {values['original_name']: new_name for new_name,
                     values in config['tables'][name]['columns'].items()}

        dataFrames[name] = dataFrame.rename(columns=new_names)
    return dataFrames