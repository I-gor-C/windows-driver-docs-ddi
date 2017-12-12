---
UID: NN.dbgeng.IDebugDataSpaces2
title: IDebugDataSpaces2
author: windows-driver-content
description: IDebugDataSpaces2 interface
old-location: debugger\idebugdataspaces2.htm
old-project: debugger
ms.assetid: a8548f9c-5cb6-4a13-b37c-da28d316b8e1
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: DebugCreateEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugDataSpaces2
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
---

# IDebugDataSpaces2 interface



## -description

## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugDataSpaces2</b> interface inherits from <a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>. <b>IDebugDataSpaces2</b> also has these types of members:

The <b>IDebugDataSpaces2</b> interface has these methods.

Writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled.

Writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled.

 Returns the physical addresses of the system paging structures at different levels of the paging hierarchy.

Provides information about the specified pages in the target's virtual address space.

Retrieves information about a system object specified by a system handle.


Translates a location in the target's virtual address space into a physical memory address.

 


## -members
The <b>IDebugDataSpaces2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.fillphysical">FillPhysical</a>
</td>
<td align="left" width="63%">
Writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.fillvirtual">FillVirtual</a>
</td>
<td align="left" width="63%">
Writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.getvirtualtranslationphysicaloffsets">GetVirtualTranslationPhysicalOffsets</a>
</td>
<td align="left" width="63%">
 Returns the physical addresses of the system paging structures at different levels of the paging hierarchy.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.queryvirtual">QueryVirtual</a>
</td>
<td align="left" width="63%">
Provides information about the specified pages in the target's virtual address space.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.readhandledata">ReadHandleData</a>
</td>
<td align="left" width="63%">
Retrieves information about a system object specified by a system handle.


</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.virtualtophysical">VirtualToPhysical</a>
</td>
<td align="left" width="63%">
Translates a location in the target's virtual address space into a physical memory address.

</td>
</tr>
</table>Writes a pattern of bytes to the target's physical memory. The pattern is written repeatedly until the specified memory range is filled.

Writes a pattern of bytes to the target's virtual memory. The pattern is written repeatedly until the specified memory range is filled.

 Returns the physical addresses of the system paging structures at different levels of the paging hierarchy.

Provides information about the specified pages in the target's virtual address space.

Retrieves information about a system object specified by a system handle.


Translates a location in the target's virtual address space into a physical memory address.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces2 interface%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

