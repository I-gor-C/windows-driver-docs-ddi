---
UID : NE:ksmedia.KSCAMERA_EXTENDEDPROP_MetadataAlignment
title : KSCAMERA_EXTENDEDPROP_MetadataAlignment
author : windows-driver-content
description : This enumeration contains identifiers for the metadata alignment.
old-location : stream\kscamera_extendedprop_metadataalignment.htm
old-project : stream
ms.assetid : A122F923-D98E-4D73-896A-551A233E7491
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSCAMERA_EXTENDEDPROP_MetadataAlignment_64, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_32, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_64, stream.kscamera_extendedprop_metadataalignment, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_16, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024, KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192, KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024, KSCAMERA_EXTENDEDPROP_MetadataAlignment_512, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_512, KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096, KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048, KSCAMERA_EXTENDEDPROP_MetadataAlignment, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_128, KSCAMERA_EXTENDEDPROP_MetadataAlignment_32, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048, KSCAMERA_EXTENDEDPROP_MetadataAlignment_16, KSCAMERA_EXTENDEDPROP_MetadataAlignment_128, KSCAMERA_EXTENDEDPROP_MetadataAlignment_256, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192, KSCAMERA_EXTENDEDPROP_MetadataAlignment enumeration [Streaming Media Devices], ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_256, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096, ksmedia/KSCAMERA_EXTENDEDPROP_MetadataAlignment
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ksmedia.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : KSCAMERA_EXTENDEDPROP_MetadataAlignment
---

# KSCAMERA_EXTENDEDPROP_MetadataAlignment Enumeration
This enumeration contains identifiers for the metadata alignment.

## Syntax
````
typedef enum  { 
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_16    = 4,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_32,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_64,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_128,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_256,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_512,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096,
  KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192
} KSCAMERA_EXTENDEDPROP_MetadataAlignment;
````

## Constants

<table>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_1024</td>
<td>This identifies an alignment of 1024 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_128</td>
<td>This identifies an alignment of 128 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_16</td>
<td>This identifies an alignment of 16 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_2048</td>
<td>This identifies an alignment of 2048 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_256</td>
<td>This identifies an alignment of 256 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_32</td>
<td>This identifies an alignment of 32 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_4096</td>
<td>This identifies an alignment of 4096 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_512</td>
<td>This identifies an alignment of 512 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_64</td>
<td>This identifies an alignment of 64 bytes.</td>
</tr>

<tr>
<td>KSCAMERA_EXTENDEDPROP_MetadataAlignment_8192</td>
<td>This identifies an alignment of 8192 bytes.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |