---
UID: NS.mpiowmi._DSM_VERSION
title: DSM_VERSION
author: windows-driver-content
description: The DSM_VERSION structure represents version information that is associated with a DSM binary or package.
old-location: storage\dsm_version.htm
old-project: storage
ms.assetid: 1aa264fa-b552-41a0-bd43-a62f8f2b533b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DSM_VERSION, DSM_VERSION, *PDSM_VERSION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: mpiowmi.h
req.include-header: Mpiowmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DSM_VERSION
req.alt-loc: mpiowmi.h
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

# DSM_VERSION structure



## -description
<p>The DSM_VERSION structure represents version information that is associated with a DSM binary or package. While this assumes that a DSM's version will be of the type MajorVersion.MinorVersion.ProductBuild.QfeNumber, it is not mandatory for the DSM to follow this convention. The DSM must, however, fill in zeros for the fields its does not support.</p>


## -syntax

````
typedef struct _DSM_VERSION {
  ULONG MajorVersion;
  ULONG MinorVersion;
  ULONG ProductBuild;
  ULONG QfeNumber;
} DSM_VERSION, *PDSM_VERSION;
````


## -struct-fields
<dl>

### -field <b>MajorVersion</b>

<dd>
<p>An unsigned 32-bitfield that represents the major version portion of the version.</p>
</dd>

### -field <b>MinorVersion</b>

<dd>
<p>An unsigned 32-bitfield that represents the minor version portion of the version.</p>
</dd>

### -field <b>ProductBuild</b>

<dd>
<p>An unsigned 32-bitfield that represents the product build portion of the version.</p>
</dd>

### -field <b>QfeNumber</b>

<dd>
<p>An unsigned 32-bitfield that represents the QFE number portion of the version.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mpiowmi.h (include Mpiowmi.h)</dt>
</dl>
</td>
</tr>
</table>