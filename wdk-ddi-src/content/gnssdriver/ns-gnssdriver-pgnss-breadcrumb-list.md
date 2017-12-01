---
UID: NS.gnssdriver.PGNSS_BREADCRUMB_LIST
title: PGNSS_BREADCRUMB_LIST
author: windows-driver-content
description: This structure contains the response to an IOCTL_GNSS_POP_BREADCRUMBS.
old-location: sensors\gnss_breadcrumb_list.htm
old-project: sensors
ms.assetid: 40C11C4B-2FFE-452F-AA08-2BCD4B6A4F7F
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PGNSS_BREADCRUMB_LIST, GNSS_BREADCRUMB_LIST, *PGNSS_BREADCRUMB_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_BREADCRUMB_LIST
req.alt-loc: gnssdriver.h
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

# PGNSS_BREADCRUMB_LIST structure



## -description
<p>This structure contains the response to an <a href="..\gnssdriver\ni-gnssdriver-ioctl-gnss-pop-breadcrumbs.md">IOCTL_GNSS_POP_BREADCRUMBS</a>.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  ULONG NumCrumbs;
  union {
    GNSS_BREADCRUMB_V1  v1[50];
  };
} GNSS_BREADCRUMB_LIST, *PGNSS_BREADCRUMB_LIST;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>NumCrumbs</b>

<dd>
<p>The number of breadcrumbs in the <b>IOCTL_GNSS_POP_BREADCRUMBS</b> response.</p>
</dd>

### -field <b> v1[50]</b>

<dd>
<p>An array of individual breadcrumbs returned in the in the <b>IOCTL_GNSS_POP_BREADCRUMBS</b> response.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>