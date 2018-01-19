---
UID : NS:ntifs._FILE_MODE_INFORMATION
title : _FILE_MODE_INFORMATION
author : windows-driver-content
description : The FILE_MODE_INFORMATION structure is used to query or set the access mode of a file.
old-location : kernel\file_mode_information.htm
old-project : kernel
ms.assetid : c01ee792-4e39-4135-b389-a5c5ac832245
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _FILE_MODE_INFORMATION, *PFILE_MODE_INFORMATION, FILE_MODE_INFORMATION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Ntifs.h, Fltkernel.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows XP and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FILE_MODE_INFORMATION
req.alt-loc : Ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PFILE_MODE_INFORMATION, FILE_MODE_INFORMATION"
---

# _FILE_MODE_INFORMATION structure
The <b>FILE_MODE_INFORMATION</b> structure is used to query or set the access mode of a file.

## Syntax
````
typedef struct _FILE_MODE_INFORMATION {
  ULONG Mode;
} FILE_MODE_INFORMATION, *PFILE_MODE_INFORMATION;
````

## Members

        
            `Mode`

            Specifies the mode in which the file will be accessed following a create-file or open-file operation. This parameter is either zero or the bitwise OR of one or more of the following file option flags:

    ## Remarks
        This structure contains a set of flags that specify the mode in which the file can be accessed. These flags are a subset of the options that can be specified in the <i>CreateOptions</i> parameter of the <a href="..\wdm\nf-wdm-iocreatefile.md">IoCreateFile</a> routine.

This structure is used by the <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> routine.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

    ## See Also

        <dl>
<dt>
<a href="..\wdm\nf-wdm-iocreatefile.md">IoCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FILE_MODE_INFORMATION structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>