---
UID: NS.d3dkmddi._DXGKCB_NOTIFY_MPO_VSYNC_FLAGS
title: DXGKCB_NOTIFY_MPO_VSYNC_FLAGS
author: windows-driver-content
description: A structure containing the flags set by the driver to process a flip entry.
old-location: display\dxgkcb_notify_mpo_vsync_flags.htm
old-project: display
ms.assetid: 5583297C-D927-4D9A-8F77-D9871B2CA736
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKCB_NOTIFY_MPO_VSYNC_FLAGS, DXGKCB_NOTIFY_MPO_VSYNC_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKCB_NOTIFY_MPO_VSYNC_FLAGS
req.alt-loc: d3dkmddi.h
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

# DXGKCB_NOTIFY_MPO_VSYNC_FLAGS structure



## -description
<p>A structure containing the flags set by the driver to process a flip entry.</p>


## -syntax

````
typedef struct _DXGKCB_NOTIFY_MPO_VSYNC_FLAGS {
  union {
    struct {
      UINT PostPresentNeeded  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGKCB_NOTIFY_MPO_VSYNC_FLAGS;
````


## -struct-fields
<dl>

### -field <b>PostPresentNeeded</b>

<dd>
<p>The driver sets this flag to indicate that scheduler must call DXGDDI_POSTMULTIPLANEOVERLAYPRESENT for this flip entry. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 31 bits (0xFFFFFFFE) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd></dd>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>