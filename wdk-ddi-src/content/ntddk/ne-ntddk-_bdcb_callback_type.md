---
UID: NE:ntddk._BDCB_CALLBACK_TYPE
title: "_BDCB_CALLBACK_TYPE"
author: windows-driver-content
description: The BDCB_CALLBACK_TYPE enumeration specifies whether the callback being passed to a BOOT_DRIVER_CALLBACK_FUNCTION routine is a status update or a boot-start driver initialization notification.
old-location: kernel\bdcb_callback_type.htm
old-project: kernel
ms.assetid: 22698DF4-7B8C-40B8-9B07-EEDCC03D0D0F
ms.author: windowsdriverdev
ms.date: 1/4/2018
ms.keywords: ntddk/BDCB_CALLBACK_TYPE, kernel.bdcb_callback_type, BdCbStatusUpdate, _BDCB_CALLBACK_TYPE, BDCB_CALLBACK_TYPE, BDCB_CALLBACK_TYPE enumeration [Kernel-Mode Driver Architecture], ntddk/BdCbInitializeImage, ntddk/BdCbStatusUpdate, *PBDCB_CALLBACK_TYPE, BdCbInitializeImage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ntddk.h
apiname:
-	BDCB_CALLBACK_TYPE
product: Windows
targetos: Windows
req.typenames: "*PBDCB_CALLBACK_TYPE, BDCB_CALLBACK_TYPE"
---

# _BDCB_CALLBACK_TYPE Enumeration
The BDCB_CALLBACK_TYPE enumeration specifies  whether the callback being passed to a <a href="..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md">BOOT_DRIVER_CALLBACK_FUNCTION</a> routine is a status update or a boot-start driver initialization notification.

## Syntax
````
typedef enum _BDCB_CALLBACK_TYPE { 
  BdCbStatusUpdate,
  BdCbInitializeImage
} BDCB_CALLBACK_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>BdCbInitializeImage</td>
                    <td>A boot image is about to be initialized. During this callback, boot-start drivers may classify a boot image as a known good image or a known bad image.</td>
                </tr>
            
                <tr>
                    <td>BdCbStatusUpdate</td>
                    <td>A status update provided by the system to a boot-start driver.</td>
                </tr>
</table>

    ## Remarks

        The two callback types have unique context structures that provide additional information specific to the callback.
<table>
<tr>
<th>Value </th>
<th>Corresponding structure to use</th>
</tr>
<tr>
<td>
BdCbStatusUpdate

</td>
<td>

<a href="..\ntddk\ne-ntddk-_bdcb_status_update_type.md">BDCB_STATUS_UPDATE_TYPE</a>


</td>
</tr>
<tr>
<td>
BdCbInitializeImage

</td>
<td>

<a href="..\ntddk\ne-ntddk-_bdcb_classification.md">BDCB_CLASSIFICATION</a>


</td>
</tr>
</table>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with  Windows 8. Available starting with  Windows 8. |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <a href="..\ntddk\nf-ntddk-ioregisterbootdrivercallback.md">BOOT_DRIVER_CALLBACK_FUNCTION</a>

<a href="..\ntddk\ne-ntddk-_bdcb_classification.md">BDCB_CLASSIFICATION</a>

<a href="..\ntddk\ne-ntddk-_bdcb_status_update_type.md">BDCB_STATUS_UPDATE_TYPE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20BDCB_CALLBACK_TYPE enumeration%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>