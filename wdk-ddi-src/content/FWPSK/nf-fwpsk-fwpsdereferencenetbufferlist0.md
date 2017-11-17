---
UID: NF.fwpsk.FwpsDereferenceNetBufferList0
title: FwpsDereferenceNetBufferList0
author: windows-driver-content
description: The FwpsDereferenceNetBufferList0 function decrements the reference count for a NET_BUFFER_LIST structure that a callout driver had acquired earlier using the FwpsReferenceNetBufferList0 function.Note  FwpsDereferenceNetBufferList0 is a specific version of FwpsDereferenceNetBufferList. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwpsdereferencenetbufferlist0.htm
ms.assetid: e327fe9d-9425-4cc3-9552-88e9c4c3bdbe
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsDereferenceNetBufferList0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsDereferenceNetBufferList0
req.iface: 
---

# FwpsDereferenceNetBufferList0 function



## -description
<p>The 
  <b>FwpsDereferenceNetBufferList0</b> function decrements the reference count for a 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that a callout
  driver had acquired earlier using the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551206">FwpsReferenceNetBufferList0</a> function.</p>


## -syntax

````
void NTAPI FwpsDereferenceNetBufferList0(
  _Inout_ NET_BUFFER_LIST *netBufferList,
  _In_    BOOLEAN         dispatchLevel
);
````


## -parameters
<dl>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for which the
     reference count is being decremented.</p>
</dd>

### -param <i>dispatchLevel</i> [in]

<dd>
<p>A value that indicates that the current IRQL = DISPATCH_LEVEL. A callout driver should set this
     parameter to <b>TRUE</b> only if it is known that it is running at IRQL = DISPATCH_LEVEL. Otherwise a callout
     driver sets this parameter to <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsDereferenceNetBufferList0</b> function to decrement the reference count for a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it had
    acquired earlier using the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551206">FwpsReferenceNetBufferList0</a> function. A callout driver must not call the 
    <b>FwpsDereferenceNetBufferList0</b> function for a NET_BUFFER_LIST structure unless it previously called
    the 
    <b>
    FwpsReferenceNetBufferList0</b> for the same structure.</p>

<p>A callout driver calls the 
    <b>FwpsDereferenceNetBufferList0</b> function to decrement the reference count for a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that it had
    acquired earlier using the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551206">FwpsReferenceNetBufferList0</a> function. A callout driver must not call the 
    <b>FwpsDereferenceNetBufferList0</b> function for a NET_BUFFER_LIST structure unless it previously called
    the 
    <b>
    FwpsReferenceNetBufferList0</b> for the same structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551206">FwpsReferenceNetBufferList0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsDereferenceNetBufferList0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
