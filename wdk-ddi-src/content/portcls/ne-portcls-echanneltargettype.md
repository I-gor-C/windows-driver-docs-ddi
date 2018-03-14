---
UID: NE:portcls.eChannelTargetType
title: eChannelTargetType
author: windows-driver-content
description: The eChannelTargetType enumeration defines constants that specify a type of node (target) in a given channel.
old-location: audio\echanneltargettype.htm
old-project: audio
ms.assetid: 44C5BE49-E8D5-4E6C-BDC5-494F180D580A
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: audio.echanneltargettype, eChannelTargetType, eChannelTargetType enumeration [Audio Devices], eMuteAttribute, ePeakMeterAttribute, eVolumeAttribute, portcls/eChannelTargetType, portcls/eMuteAttribute, portcls/ePeakMeterAttribute, portcls/eVolumeAttribute
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: portcls.h
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
-	Portcls.h
api_name:
-	eChannelTargetType
product: Windows
targetos: Windows
req.typenames: eChannelTargetType
---

# eChannelTargetType Enumeration
The <b>eChannelTargetType</b> enumeration defines constants that specify a type of node (target) in a given channel.

## Syntax
````
typedef enum _eChannelTargetType { 
  eVolumeAttribute,
  eMuteAttribute,
  ePeakMeterAttribute
} eChannelTargetType;
````

## Constants

<table>
            
                <tr>
                    <td>eMuteAttribute</td>
                    <td>Indicates a Mute node.</td>
                </tr>
            
                <tr>
                    <td>ePeakMeterAttribute</td>
                    <td>Indicates a PeakMeter node.</td>
                </tr>
            
                <tr>
                    <td>eVolumeAttribute</td>
                    <td>Indicates a volume level control node.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | portcls.h |