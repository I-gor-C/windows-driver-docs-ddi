---
UID: NN.wudfddi.IWDFMemory~r1
title: IWDFMemory
author: windows-driver-content
description: The IWDFMemory interface exposes the framework memory object that provides access to a memory block.
old-location: wdf\iwdfmemory.htm
old-project: wdf
ms.assetid: 8746eb43-7a6e-4e1d-b8fb-c8b7891295d6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFWorkItem, GetParentObject, IWDFWorkItem::GetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFMemory
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFWorkItem
req.product: Windows 10 or later.
---

# IWDFMemory interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFMemory</b> interface exposes the framework memory object that provides access to a memory block.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFMemory</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFMemory</b> also has these types of members:</p>

<p>The <b>IWDFMemory</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfmemory_copyfrombuffer">CopyFromBuffer</a> method safely copies data from the specified source buffer to a memory object.</p>

<p>The <a href="wdf.iwdfmemory_copyfrommemory">CopyFromMemory</a> method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.</p>

<p>The <a href="wdf.iwdfmemory_copytobuffer">CopyToBuffer</a> method safely copies data from a memory object to the specified target buffer.</p>

<p>The <a href="wdf.iwdfmemory_getdatabuffer">GetDataBuffer</a> method retrieves the data buffer that is associated with a memory object.</p>

<p>The <a href="wdf.iwdfmemory_getsize">GetSize</a> method retrieves the size of the data buffer that is associated with a memory object.</p>

<p>The <a href="wdf.iwdfmemory_setbuffer">SetBuffer</a> method assigns a specified buffer to a memory object that a driver created by calling <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">IWDFDriver::CreatePreallocatedWdfMemory</a>. </p>

<p> </p>

## -members
<p>The <b>IWDFMemory</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_copyfrombuffer">IWDFMemory::CopyFromBuffer</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_copyfrombuffer">CopyFromBuffer</a> method safely copies data from the specified source buffer to a memory object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_copyfrommemory">IWDFMemory::CopyFromMemory</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_copyfrommemory">CopyFromMemory</a> method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_copytobuffer">IWDFMemory::CopyToBuffer</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_copytobuffer">CopyToBuffer</a> method safely copies data from a memory object to the specified target buffer.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_getdatabuffer">IWDFMemory::GetDataBuffer</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_getdatabuffer">GetDataBuffer</a> method retrieves the data buffer that is associated with a memory object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_getsize">IWDFMemory::GetSize</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_getsize">GetSize</a> method retrieves the size of the data buffer that is associated with a memory object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfmemory_setbuffer">IWDFMemory::SetBuffer</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfmemory_setbuffer">SetBuffer</a> method assigns a specified buffer to a memory object that a driver created by calling <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">IWDFDriver::CreatePreallocatedWdfMemory</a>. </p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfmemory_copyfrombuffer">CopyFromBuffer</a> method safely copies data from the specified source buffer to a memory object.</p>

<p>The <a href="wdf.iwdfmemory_copyfrommemory">CopyFromMemory</a> method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.</p>

<p>The <a href="wdf.iwdfmemory_copytobuffer">CopyToBuffer</a> method safely copies data from a memory object to the specified target buffer.</p>

<p>The <a href="wdf.iwdfmemory_getdatabuffer">GetDataBuffer</a> method retrieves the data buffer that is associated with a memory object.</p>

<p>The <a href="wdf.iwdfmemory_getsize">GetSize</a> method retrieves the size of the data buffer that is associated with a memory object.</p>

<p>The <a href="wdf.iwdfmemory_setbuffer">SetBuffer</a> method assigns a specified buffer to a memory object that a driver created by calling <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">IWDFDriver::CreatePreallocatedWdfMemory</a>. </p>

<p> </p>

## -remarks


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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>