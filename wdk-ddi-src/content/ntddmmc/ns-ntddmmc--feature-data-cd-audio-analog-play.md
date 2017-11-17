---
UID: NS.ntddmmc._FEATURE_DATA_CD_AUDIO_ANALOG_PLAY
title: FEATURE_DATA_CD_AUDIO_ANALOG_PLAY
author: windows-driver-content
description: The FEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure holds information about the CD Audio External Play feature.
old-location: storage\feature_data_cd_audio_analog_play.htm
ms.assetid: 01c34bb8-b164-425d-b81c-7eefc08296e2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_CD_AUDIO_ANALOG_PLAY
req.alt-loc: ntddmmc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: FEATURE_DATA_CD_AUDIO_ANALOG_PLAY, FEATURE_DATA_CD_AUDIO_ANALOG_PLAY, *PFEATURE_DATA_CD_AUDIO_ANALOG_PLAY
req.iface: 
---

# FEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure



## -description
<p>The FEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure holds information about the CD Audio External Play feature.</p>


## -syntax

````
typedef struct _FEATURE_DATA_CD_AUDIO_ANALOG_PLAY {
  FEATURE_HEADER Header;
  UCHAR          SeperateVolume  :1;
  UCHAR          SeperateChannelMute  :1;
  UCHAR          ScanSupported  :1;
  UCHAR          Reserved1  :5;
  UCHAR          Reserved2;
  UCHAR          NumerOfVolumeLevels[2];
} FEATURE_DATA_CD_AUDIO_ANALOG_PLAY, *PFEATURE_DATA_CD_AUDIO_ANALOG_PLAY;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>SeperateVolume</b>

<dd>
<p>Indicates, when set to zero, that all audio channels have the same volume level. When set to 1, it indicates that the volume of each audio channel can be set separately. </p>
</dd>

### -field <b>SeperateChannelMute</b>

<dd>
<p>Indicates, when set to zero, that all audio channels are muted simultaneously. When set to 1, it indicates that each audio channel can be muted independently. </p>
</dd>

### -field <b>ScanSupported</b>

<dd>
<p>Indicates, when set to 1, that the SCAN command is supported. See the <i>SCSI Multimedia 3 </i>(<i>MMC-3</i>) specification for a description of the SCAN command. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>NumerOfVolumeLevels</b>

<dd></dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "CD Audio External Play" by the <i>MMC-3 </i>specification. Devices that support this feature can play CD audio data and channel it directly to an external output.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553850">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20FEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
