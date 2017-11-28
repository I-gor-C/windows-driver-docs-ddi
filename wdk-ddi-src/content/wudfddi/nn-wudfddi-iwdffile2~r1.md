---
UID: NN.wudfddi.IWDFFile2~r1
title: IWDFFile2
author: windows-driver-content
description: Drivers obtain the IWDFFile2 interface by calling IWDFFile::QueryInterface.
old-location: wdf\iwdffile2.htm
old-project: wdf
ms.assetid: 49a3defc-d86c-4d70-8c1c-a5abbadda013
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.umdf-ver: 1.9
req.alt-api: IWDFFile2
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

# IWDFFile2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>Drivers obtain the <b>IWDFFile2</b> interface by calling <b>IWDFFile::QueryInterface</b>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFFile2</b> interface inherits from <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a>. <b>IWDFFile2</b> also has these types of members:</p>

<p>The <b>IWDFFile2</b> interface has these methods.</p>

<p>The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.</p>

<p>The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. </p>

<p> </p>

## -members
<p>The <b>IWDFFile2</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558917">IWDFFile2::GetRelatedFileObject</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558920">IWDFFile2::RetrieveCountedFileName</a>
</td>
<td align="left" width="63%">
<p>The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. </p>
</td>
</tr>
</table><p>The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.</p>

<p>The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. </p>

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
<p>1.9</p>
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