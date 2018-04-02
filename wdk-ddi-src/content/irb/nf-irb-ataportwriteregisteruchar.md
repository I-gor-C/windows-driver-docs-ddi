---
UID: NF:irb.AtaPortWriteRegisterUchar
title: AtaPortWriteRegisterUchar function
author: windows-driver-content
description: The AtaPortWriteRegisterUchar routine transfers an unsigned byte to the HBA.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportwriteregisteruchar.htm
old-project: storage
ms.assetid: c7c887e6-6861-4366-b8b4-fe6292ac5c99
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: AtaPortWriteRegisterUchar, AtaPortWriteRegisterUchar routine [Storage Devices], atartns_14d5eb64-a6b7-4eb4-94f6-0bd0952d2263.xml, irb/AtaPortWriteRegisterUchar, storage.ataportwriteregisteruchar
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
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
req.lib: Ataport.lib; Pciidex.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	ataport.lib
-	ataport.dll
-	pciidex.lib
-	pciidex.dll
api_name:
-	AtaPortWriteRegisterUchar
product:
- Windows
targetos: Windows
req.typenames: IDE_POWER_STATE
---


# AtaPortWriteRegisterUchar function
The <b>AtaPortWriteRegisterUchar</b> routine transfers an unsigned byte to the HBA.
<div class="alert"><b>Note</b>  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax

```
void AtaPortWriteRegisterUchar(
  PUCHAR Register,
  UCHAR  Value
);
```

## Parameters

`Register`

A pointer to the destination register. The address value that is assigned to this parameter must be within the range of mapped I/O space addresses that are obtained by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff550160">AtaPortGetDeviceBase</a>.

`Value`

Specifies the value to write to the register for the HBA.


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | irb.h (include Ata.h, Irb.h) |
| **Library** | Ataport.lib; Pciidex.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550160">AtaPortGetDeviceBase</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550280">AtaPortWriteRegisterUlong</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550287">AtaPortWriteRegisterUshort</a>