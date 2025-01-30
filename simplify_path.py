def simplifyPath(path: str) -> str:
    paths = []
    current_path = ""
    for char in path + "/":
        if char == "/":
            if current_path == "..":
                if paths:
                    paths.pop()
            elif current_path and current_path != ".":
                paths.append(current_path)
            current_path = ""
        else:
            current_path += char

    return "/" + "/".join(paths)

print(simplifyPath("/home//foo"))