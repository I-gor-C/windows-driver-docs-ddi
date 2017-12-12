---
UID: NN.wudfddi.IWDFFile2~r1
title: IWDFFile2
author: windows-driver-content
description: Drivers obtain the IWDFFile2 interface by calling IWDFFile::QueryInterface.
old-location: wdf\iwdffile2.htm
old-project: wdf
ms.assetid: 49a3defc-d86c-4d70-8c1c-a5abbadda013
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, POWER_ACTION, *PPOWER_ACTION
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
req.product: Windows 10 or later.
---

# IWDFFile2 interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

Drivers obtain the <b>IWDFFile2</b> interface by calling <b>IWDFFile::QueryInterface</b>.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFFile2</b> interface inherits from <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a>. <b>IWDFFile2</b> also has these types of members:

The <b>IWDFFile2</b> interface has these methods.

The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.

The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. 

 


## -members
The <b>IWDFFile2</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdffile2_getrelatedfileobject">IWDFFile2::GetRelatedFileObject</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdffile2_retrievecountedfilename">IWDFFile2::RetrieveCountedFileName</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. 

</td>
</tr>
</table>The <a href="wdf.iwdffile2_getrelatedfileobject">GetRelatedFileObject</a> method retrieves the <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface of a <i>related file object</i>, which is a file object that has a technology-specific relationship with another file object.

The <a href="wdf.iwdffile2_retrievecountedfilename">RetrieveCountedFileName</a> method retrieves the full counted file name for a file that is associated with a device. 

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.9

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>