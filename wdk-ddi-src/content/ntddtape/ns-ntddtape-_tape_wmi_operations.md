---
UID : NS:ntddtape._TAPE_WMI_OPERATIONS
title : _TAPE_WMI_OPERATIONS
author : windows-driver-content
description : The tape miniclass driver passes this structure to its TapeMiniWMIControl routine to indicate which WMI operation must be performed by the device.
old-location : storage\tape_wmi_operations.htm
old-project : storage
ms.assetid : 430d982e-4740-46ad-8391-aba5813a833a
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _TAPE_WMI_OPERATIONS, TAPE_WMI_OPERATIONS, *PTAPE_WMI_OPERATIONS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddtape.h
req.include-header : Ntddchgr.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : TAPE_WMI_OPERATIONS
req.alt-loc : ntddtape.h
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
req.typenames : TAPE_WMI_OPERATIONS, *PTAPE_WMI_OPERATIONS
---

# _TAPE_WMI_OPERATIONS structure
The tape miniclass driver passes this structure to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff567957">TapeMiniWMIControl</a> routine to indicate which WMI operation must be performed by the device.

## Syntax
````
typedef struct _TAPE_WMI_OPERATIONS {
  ULONG Method;
  ULONG DataBufferSize;
  PVOID DataBuffer;
} TAPE_WMI_OPERATIONS, *PTAPE_WMI_OPERATIONS;
````

## Members

        
            `DataBuffer`

            Pointer to a buffer in which the tape minidriver returns the results of the operation. The first <b>sizeof</b>(ULONG) bytes of <b>DataBuffer</b> contain a value of type <a href="..\ntddtape\ne-ntddtape-_tape_drive_problem_type.md">TAPE_DRIVE_PROBLEM_TYPE</a>, followed by <b>DataBufferSize</b> - <b>sizeof</b>(ULONG) bytes of tape data.
        
            `DataBufferSize`

            Indicates the size in bytes of the buffer in which the tape minidriver returns the results of the operation.
        
            `Method`

            Indicates the operation to be performed by the tape device. The operations allowed are as follows:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddtape.h (include Ntddchgr.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567957">TapeMiniWMIControl</a>
</dt>
<dt>
<a href="..\ntddtape\ne-ntddtape-_tape_drive_problem_type.md">TAPE_DRIVE_PROBLEM_TYPE</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20TAPE_WMI_OPERATIONS structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>