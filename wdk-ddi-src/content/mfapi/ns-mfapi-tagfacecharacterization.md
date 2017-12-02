---
UID: NS.mfapi.tagFaceCharacterization
title: tagFaceCharacterization
author: windows-driver-content
description: The FaceCharacterization structure describes the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute.
old-location: stream\facecharacterization.htm
old-project: stream
ms.assetid: 8A8F6E06-DA09-4595-BF42-8B905453CCCA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagFaceCharacterization, FaceCharacterization
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
req.alt-api: FaceCharacterization
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
req.iface: 
---

# tagFaceCharacterization structure



## -description
<p>The <b>FaceCharacterization</b> structure describes the blob format for the <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute.</p>


## -syntax

````
typedef struct tagFaceCharacterization {
  ULONG BlinkScoreLeft;
  ULONG BlinkScoreRight;
  ULONG FacialExpression;
  ULONG FacialExpressionScore;
} FaceCharacterization;
````


## -struct-fields
<dl>

### -field BlinkScoreLeft

<dd>
<p>0 indicates no blink for the left eye, 100 indicates definite blink for the left eye (0 - 100).</p>
</dd>

### -field BlinkScoreRight

<dd>
<p>0 indicates no blink for the right eye, 100 indicates definite blink for the right eye (0 - 100).</p>
</dd>

### -field FacialExpression

<dd>
<p>A  defined facial expression value.</p>
</dd>

### -field FacialExpressionScore

<dd>
<p>0 indicates no such facial expression as identified, 100 indicates definite such facial expression as defined (0 - 100).</p>
</dd>
</dl>

## -remarks
<p>The <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute contains the blink and facial expression state for the face ROIs identified in <b>MF_CAPTURE_METADATA_FACEROIS</b>.  For a  device that does not support blink or facial expression detection, this attribute should be omitted.</p>

<p>The facial expressions that can be detected are defined as follows:</p>

<p>The <a href="stream.facecharacterizationblobheader">FaceCharacterizationBlobHeader</a> and <b>FaceCharacterization</b> structures only describe the blob format for the <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute.  The metadata item structure for the face characterizations (<a href="stream.kscamera_metadata_itemheader">KSCAMERA_METADATA_ITEMHEADER</a> + face characterizations metadata payload) is up to driver and must be 8-byte aligned. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mfapi.h</dt>
</dl>
</td>
</tr>
</table>