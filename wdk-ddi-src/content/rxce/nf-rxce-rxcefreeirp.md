---
UID: NF.rxce.RxCeFreeIrp
title: RxCeFreeIrp
author: windows-driver-content
description: RxCeFreeIrp frees an IRP.
old-location: ifsk\rxcefreeirp.htm
old-project: ifsk
ms.assetid: 71e3283c-2dbc-4579-a374-e51e123b852f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxCeFreeIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: rxce.h
req.include-header: Rxce.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxCeFreeIrp
req.alt-loc: rxce.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RxCeFreeIrp function



## -description
<p><b>RxCeFreeIrp</b> frees an IRP.</p>


## -syntax

````
VOID RxCeFreeIrp(
   PIRP pIrp
);
````


## -parameters
<dl>

### -param pIrp 

<dd>
<p>A pointer to the IRP to be freed.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>An IRP allocated with an associated memory descriptor list allocated with <b>RxCeAllocateIrpWithMDL</b> should be freed when the IRP is completed using <b>RxCeFreeIrp</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Rxce.h (include Rxce.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\rxce\nf-rxce-rxceallocateirpwithmdl.md">RxCeAllocateIrpWithMDL</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--mdl.md">MDL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxCeFreeIrp function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
