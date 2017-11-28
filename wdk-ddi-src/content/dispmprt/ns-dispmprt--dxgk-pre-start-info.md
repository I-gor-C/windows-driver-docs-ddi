---
UID: NS.dispmprt._DXGK_PRE_START_INFO
title: DXGK_PRE_START_INFO
author: windows-driver-content
description: Structure to allow very simple data to be exchanged between the OS and driver which may be required prior to start device being called and therefore cannot be queried through normal caps or adapter info DDIs.
old-location: display\dxgk_pre_start_info.htm
old-project: display
ms.assetid: 4CCDA951-A583-48C4-98D7-D278183D8893
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_PRE_START_INFO, DXGK_PRE_START_INFO, *PDXGK_PRE_START_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dispmprt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_PRE_START_INFO
req.alt-loc: dispmprt.h
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

# DXGK_PRE_START_INFO structure



## -description
<p>Structure to allow very simple data to be exchanged between the OS and driver which may be required prior to start device being called and therefore cannot be queried through normal caps or adapter info DDIs.</p>


## -syntax

````
typedef struct _DXGK_PRE_START_INFO {
  union {
    struct {
      UINT ReservedIn;
    };
    UINT Input;
  };
  union {
    struct {
      UINT SupportPreserveBootDisplay  :1;
      UINT IsUEFIFrameBufferCpuAccessibleDuringStartup  :1;
      UINT ReservedOut  :30;
    };
    UINT Output;
  };
} DXGK_PRE_START_INFO, *PDXGK_PRE_START_INFO;
````


## -struct-fields
<dl>

### -field <b>ReservedIn</b>

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field <b>Input</b>

<dd>
<p>The combined UINT value operated on.</p>
</dd>

### -field <b>SupportPreserveBootDisplay</b>

<dd>
<p>Flag which indicates support for preserving the timing and content of the firmware display mode across DxgkDdiStartDevice.</p>
</dd>

### -field <b>IsUEFIFrameBufferCpuAccessibleDuringStartup</b>

<dd>
<p>Indicates that the driver can maintain same CPU virtual address mapping to the UEFI frame buffer during driver initialization.</p>
</dd>

### -field <b>ReservedOut</b>

<dd>
<p>This value is reserved for system use.</p>
</dd>

### -field <b>Output</b>

<dd>
<p>The combined UINT value operated on.</p>
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
<dt>Dispmprt.h</dt>
</dl>
</td>
</tr>
</table>