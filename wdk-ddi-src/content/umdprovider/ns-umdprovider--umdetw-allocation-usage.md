---
UID: NS.umdprovider._UMDETW_ALLOCATION_USAGE
title: UMDETW_ALLOCATION_USAGE
author: windows-driver-content
description: Indicates the reason for mapping from a Microsoft Direct3D memory allocation to a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) allocation.
old-location: display\umdetw_allocation_usage.htm
old-project: display
ms.assetid: 40522471-0fbc-4193-8164-60138e3862fe
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: UMDETW_ALLOCATION_USAGE, UMDETW_ALLOCATION_USAGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: umdprovider.h
req.include-header: Umdprovider.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UMDETW_ALLOCATION_USAGE
req.alt-loc: umdprovider.h
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
req.product: Windows 10 or later.
---

# UMDETW_ALLOCATION_USAGE structure



## -description
<p>Indicates the reason for mapping from a Microsoft Direct3D  memory allocation to a Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) allocation.</p>


## -syntax

````
typedef struct _UMDETW_ALLOCATION_USAGE {
  union {
    struct {
      UINT Packed  :1;
      UINT Renamed  :1;
      UINT Reserved  :14;
      UINT DriverReserved  :16;
    };
    UINT   Value;
  };
} UMDETW_ALLOCATION_USAGE;
````


## -struct-fields
<dl>

### -field <b>Packed</b>

<dd>
<p>The allocation is packed into a larger parent allocation.</p>
</dd>

### -field <b>Renamed</b>

<dd>
<p>The allocation is a renamed instance of a Direct3D allocation.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
</dd>

### -field <b>DriverReserved</b>

<dd>
<p>The driver can use these bit fields for its own internal purposes.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that specifies the allocation mapping.</p>
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
<dt>Umdprovider.h (include Umdprovider.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj542437">UMDEtwLogMapAllocation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20UMDETW_ALLOCATION_USAGE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
