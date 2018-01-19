---
UID : NF:srb.ScsiPortReadRegisterUlong
title : ScsiPortReadRegisterUlong function
author : windows-driver-content
description : The ScsiPortReadRegisterUlong routine reads a ULONG value from the HBA.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location : storage\scsiportreadregisterulong.htm
old-project : storage
ms.assetid : e644fce4-2367-4851-8252-47a25faf0b6d
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : ScsiPortReadRegisterUlong
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : srb.h
req.include-header : Miniport.h, Scsi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : ScsiPortReadRegisterUlong
req.alt-loc : Scsiport.lib,Scsiport.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Scsiport.lib
req.dll : 
req.irql : 
req.typenames : "*PSPB_CONTROLLER_CONFIG, SPB_CONTROLLER_CONFIG"
req.product : Windows 10 or later.
---


# ScsiPortReadRegisterUlong function
The <b>ScsiPortReadRegisterUlong</b> routine reads a ULONG value from the HBA.

## Syntax

````
ULONG ScsiPortReadRegisterUlong(
  _In_ PULONG Register
);
````

## Parameters

`Register`

Pointer to the register. The given <i>Register</i> must be in a mapped memory-space range returned by <b>ScsiPortGetDeviceBase</b>.


## Return Value

<b>ScsiPortReadRegisterUlong</b> returns a ULONG value from the HBA's register.

## Remarks

<b>ScsiPortReadRegisterUlong</b> ensures that data is transferred correctly.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | srb.h (include Miniport.h, Scsi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\srb\nf-srb-scsiportgetdevicebase.md">ScsiPortGetDeviceBase</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiPortReadRegisterUlong routine%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>