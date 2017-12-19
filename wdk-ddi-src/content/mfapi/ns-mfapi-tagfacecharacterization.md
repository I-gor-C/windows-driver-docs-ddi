---
UID: NS.MFAPI.TAGFACECHARACTERIZATION
title: tagFaceCharacterization
author: windows-driver-content
description: The FaceCharacterization structure describes the blob format for the MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS attribute.
old-location: stream\facecharacterization.htm
old-project: stream
ms.assetid: 8A8F6E06-DA09-4595-BF42-8B905453CCCA
ms.author: windowsdriverdev
ms.date: 12/14/2017
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
---

# tagFaceCharacterization structure



## -description
The <b>FaceCharacterization</b> structure describes the blob format for the <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute.



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

### -field BlinkScoreLeft

0 indicates no blink for the left eye, 100 indicates definite blink for the left eye (0 - 100).


### -field BlinkScoreRight

0 indicates no blink for the right eye, 100 indicates definite blink for the right eye (0 - 100).


### -field FacialExpression

A  defined facial expression value.


### -field FacialExpressionScore

0 indicates no such facial expression as identified, 100 indicates definite such facial expression as defined (0 - 100).


## -remarks
The <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute contains the blink and facial expression state for the face ROIs identified in <b>MF_CAPTURE_METADATA_FACEROIS</b>.  For a  device that does not support blink or facial expression detection, this attribute should be omitted.

The facial expressions that can be detected are defined as follows:

The <a href="stream.facecharacterizationblobheader">FaceCharacterizationBlobHeader</a> and <b>FaceCharacterization</b> structures only describe the blob format for the <b>MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS</b> attribute.  The metadata item structure for the face characterizations (<a href="stream.kscamera_metadata_itemheader">KSCAMERA_METADATA_ITEMHEADER</a> + face characterizations metadata payload) is up to driver and must be 8-byte aligned. 


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