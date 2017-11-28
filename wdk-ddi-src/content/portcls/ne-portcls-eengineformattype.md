---
UID: NE.portcls.eEngineFormatType
title: eEngineFormatType
author: windows-driver-content
description: The eEngineFormatType enumeration defines constants that specify the audio data type supported by the audio engine.
old-location: audio\eengineformattype.htm
old-project: audio
ms.assetid: C16DE51F-6552-4379-B866-D7653B1BA9F2
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: BarcodeSymbologyAttributesData, BarcodeSymbologyAttributesData
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
req.alt-api: eEngineFormatType
req.alt-loc: Portcls.h
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
req.iface: 
---

# eEngineFormatType enumeration



## -description
<p>The <b>eEngineFormatType</b> enumeration defines constants that specify the audio data type supported by the audio engine.</p>


## -syntax

````
typedef enum _eEngineFormatType { 
  eMixFormat,
  eDeviceFormat,
  eSupportedDeviceFormats
} eEngineFormatType;
````


## -enum-fields
<dl>

### -field <a id="eMixFormat"></a><a id="emixformat"></a><a id="EMIXFORMAT"></a><b>eMixFormat</b>

<dd>
<p>Indicates a data format for the Mixer.</p>
</dd>

### -field <a id="eDeviceFormat"></a><a id="edeviceformat"></a><a id="EDEVICEFORMAT"></a><b>eDeviceFormat</b>

<dd>
<p>Indicates the default data format for the audio adapter.</p>
</dd>

### -field <a id="eSupportedDeviceFormats"></a><a id="esupporteddeviceformats"></a><a id="ESUPPORTEDDEVICEFORMATS"></a><b>eSupportedDeviceFormats</b>

<dd>
<p>Indicates all the data formats supported by the audio adapter.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn265082">GetEngineFormatSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20eEngineFormatType enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
