---
UID: NI:bthhfpddi.IOCTL_BTHHFP_MIC_SET_VOLUME
title: IOCTL_BTHHFP_MIC_SET_VOLUME
author: windows-driver-content
description: The IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL sets the volume level of the microphone for the Bluetooth device.
old-location: audio\ioctl_bthhfp_mic_set_volume.htm
old-project: audio
ms.assetid: 438BB68B-9E09-4033-B38E-C1C28D00D43C
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IOCTL_BTHHFP_MIC_SET_VOLUME, IOCTL_BTHHFP_MIC_SET_VOLUME control code [Audio Devices], audio.ioctl_bthhfp_mic_set_volume, bthhfpddi/IOCTL_BTHHFP_MIC_SET_VOLUME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Bthhfpddi.h
api_name:
-	IOCTL_BTHHFP_MIC_SET_VOLUME
product:
- Windows
targetos: Windows
req.typenames: HFP_BYPASS_CODEC_ID_VERSION, *PHFP_BYPASS_CODEC_ID_VERSION
---

# IOCTL_BTHHFP_MIC_SET_VOLUME IOCTL
The <b>IOCTL_BTHHFP_MIC_SET_VOLUME</b> 
   IOCTL sets the  volume level of the microphone for the Bluetooth device.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
A LONG that represents the volume level in 1/65536 decibels.

### Input Buffer Length
The size of a LONG.

### Output Buffer
N/A

### Output Buffer Length
N/A

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
N/A

## Remarks
The audio driver sends this request when handling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a> property for the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a> node in the KS topology of the microphone path. The request’s input parameter is the same as the <b>KSPROPERTY_AUDIO_VOLUMELEVEL</b> property value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | bthhfpddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn302027">Bluetooth HFP DDI IOCTLs</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537208">KSNODETYPE_VOLUME</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537309">KSPROPERTY_AUDIO_VOLUMELEVEL</a>