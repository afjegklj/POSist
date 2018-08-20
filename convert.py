function relativePath pFilePath, pFolder
   if (the platform is "Win32" and (char 1 of pFilePath is not in  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
         or char 2 of pFilePath is not ":")) \
         or (the platform is not "Win32" and \
         char 1 of pFilePath is not "/") then
      return "Error: path is not an absolute path"
   end if
   
   if pFolder is empty then
      put the defaultFolder into pFolder
   end if
   
   if pFilePath is pFolder then
      return "."
   end if
   
   set the itemDelimiter to "/"
   repeat
      if item 1 of pFolder is item 1 of pFilePath then
         ## they're in the same disk or folder
         delete item 1 of pFilePath
         delete item 1 of pFolder
      else 
         exit repeat
      end if
   end repeat
   
   repeat for (the number of items in pFolder) times
      put "../" before pFilePath
   end repeat
     
   return pFilePath
end relativePath