---
UID: NF.dbgeng.IDebugDataSpaces4.GetNextDifferentlyValidOffsetVirtual
title: IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual
author: windows-driver-content
description: The GetNextDifferentlyValidOffsetVirtual method returns the offset of the next address whose validity might be different from the validity of the specified address.
old-location: debugger\getnextdifferentlyvalidoffsetvirtual.htm
old-project: debugger
ms.assetid: 1f55cc21-606d-4c7c-8650-51cb686700b3
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugDataSpaces4, GetNextDifferentlyValidOffsetVirtual, IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces4.GetNextDifferentlyValidOffsetVirtual
req.alt-loc: dbgeng.h
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
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual method



## -description
<p>The <b>GetNextDifferentlyValidOffsetVirtual</b> method returns the offset of the next address whose validity might be different from the validity of the specified address.</p>


## -syntax

````
HRESULT GetNextDifferentlyValidOffsetVirtual(
  [in]  ULONG64  Offset,
  [out] PULONG64 NextOffset
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies a start address.  The address returned in <i>NextOffset</i> will be the next address whose validity might be defined differently from this one.</p>
</dd>

### -param NextOffset [out]

<dd>
<p>Receives the address of the next address whose validity might be defined differently from the address in <i>Offset</i>.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>The size of regions of validity depends on the target.  For example, in live user-mode debugging sessions, where virtual address validity changes from page to page, <i>NextOffset</i> will receive the address of the next page.  In user-mode dump files the validity can change from byte to byte.</p>

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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>
</dt>
<dt>
<a href="debugger.getvalidregionvirtual">GetValidRegionVirtual</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces4::GetNextDifferentlyValidOffsetVirtual method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
