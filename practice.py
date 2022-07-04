def getBootstrapClass(screenWidth):
    # 関数を完成させてください
    if screenWidth < 768:
        return "xs"
    elif screenWidth >= 768 and screenWidth < 992:
        return "sm"
    elif screenWidth >= 992 and screenWidth < 1200:
        return "md"
    else:
        return "lg"

def screenViewMode(height,width):
    # 関数を完成させてください
    if height >= width:
        return "portrait"
    else:
        return "landscape"