---
UID: NN.wudfddi.IWDFDriver
title: IWDFDriver
author: windows-driver-content
description: The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process.
old-location: wdf\iwdfdriver.htm
old-project: wdf
ms.assetid: ada475ae-e697-475c-b461-8e3a36ae9ab1
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: IWDFDriver
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

# IWDFDriver interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>IWDFDriver</b> interface exposes the framework driver object that represents the driver image that is loaded in the host process.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFDriver</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>. <b>IWDFDriver</b> also has these types of members:</p>

<p>The <b>IWDFDriver</b> interface has these methods.</p>

<p>The <a href="wdf.iwdfdriver_createdevice">CreateDevice</a> method configures and creates a new framework device object.</p>

<p>The <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">CreatePreallocatedWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> for the specified buffer.</p>

<p>The <a href="wdf.iwdfdriver_createwdfmemory">CreateWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> and allocates, for the memory object, a data buffer of the specified nonzero size.</p>

<p>The <a href="wdf.iwdfdriver_createwdfobject">CreateWdfObject</a> method creates a custom (or user) WDF object from a parent WDF object.</p>

<p>The <a href="wdf.iwdfdriver_isversionavailable">IsVersionAvailable</a> method determines whether the specified version of the framework is available.</p>

<p>The <a href="wdf.iwdfdriver_retrieveversionstring">RetrieveVersionString</a> method retrieves the version of the framework.</p>

<p> </p>

## -members
<p>The <b>IWDFDriver</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_createdevice">IWDFDriver::CreateDevice</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_createdevice">CreateDevice</a> method configures and creates a new framework device object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_createpreallocatedwdfmemory">IWDFDriver::CreatePreallocatedWdfMemory</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">CreatePreallocatedWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> for the specified buffer.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_createwdfmemory">IWDFDriver::CreateWdfMemory</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_createwdfmemory">CreateWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> and allocates, for the memory object, a data buffer of the specified nonzero size.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_createwdfobject">IWDFDriver::CreateWdfObject</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_createwdfobject">CreateWdfObject</a> method creates a custom (or user) WDF object from a parent WDF object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_isversionavailable">IWDFDriver::IsVersionAvailable</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_isversionavailable">IsVersionAvailable</a> method determines whether the specified version of the framework is available.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfdriver_retrieveversionstring">IWDFDriver::RetrieveVersionString</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdfdriver_retrieveversionstring">RetrieveVersionString</a> method retrieves the version of the framework.</p>
</td>
</tr>
</table><p>The <a href="wdf.iwdfdriver_createdevice">CreateDevice</a> method configures and creates a new framework device object.</p>

<p>The <a href="wdf.iwdfdriver_createpreallocatedwdfmemory">CreatePreallocatedWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> for the specified buffer.</p>

<p>The <a href="wdf.iwdfdriver_createwdfmemory">CreateWdfMemory</a> method creates a <a href="wdf.framework_memory_object">framework memory object</a> and allocates, for the memory object, a data buffer of the specified nonzero size.</p>

<p>The <a href="wdf.iwdfdriver_createwdfobject">CreateWdfObject</a> method creates a custom (or user) WDF object from a parent WDF object.</p>

<p>The <a href="wdf.iwdfdriver_isversionavailable">IsVersionAvailable</a> method determines whether the specified version of the framework is available.</p>

<p>The <a href="wdf.iwdfdriver_retrieveversionstring">RetrieveVersionString</a> method retrieves the version of the framework.</p>

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