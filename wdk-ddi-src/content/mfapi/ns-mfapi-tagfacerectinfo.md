---
UID: NS.MFAPI.TAGFACERECTINFO
title: tagFaceRectInfo
author: windows-driver-content
description: The FaceRectInfo structure describes the blob format for the MF_CAPTURE_METADATA_FACEROIS attribute.
old-location: stream\facerectinfo.htm
old-project: stream
ms.assetid: 63F31CDC-CB44-4ED8-BDA0-89F7DCF77965
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: tagFaceRectInfo, FaceRectInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mfapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FaceRectInfo
req.alt-loc: mfapi.h
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
---

# tagFaceRectInfo structure



## -description
The <b>FaceRectInfo</b> structure describes the blob format for the <b>MF_CAPTURE_METADATA_FACEROIS</b> attribute.


## -syntax

````
typedef struct tagFaceRectInfo {
  RECT Region;
  LONG ConfidenceLevel;
} FaceRectInfo;
````


## -struct-fields

### -field Region

Relative coordinates on the frame that face detection is running (Q31 format).

### -field ConfidenceLevel

Confidence level of the region being a face (0 - 100).

## -remarks
The <b>MF_CAPTURE_METADATA_FACEROIS</b> attribute contains the face rectangle info detected by the driver.   By default driver\MFT0 should provide the face information on preview stream.  If the driver advertises the capability on other streams, driver\MFT must provide the face info on the corresponding streams if the application enables face detection on those streams.  When video stabilization is enabled on the driver, the face information should be provided post-video stabilization. The dominate face must be the first <b>FaceRectInfo</b> in the blob.

The <a href="stream.facerectinfoblobheader">FaceRectInfoBlobHeader</a> and <b>FaceRectInfo</b> structures only describe the blob format for the <b>MF_CAPTURE_METADATA_FACEROIS</b> attribute.  The metadata item structure for face ROIs (<a href="stream.kscamera_metadata_itemheader">KSCAMERA_METADATA_ITEMHEADER</a> + face ROIs metadata payload) is up to driver and must be 8-byte aligned.

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>