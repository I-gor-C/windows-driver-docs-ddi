---
UID: NN.wudfddi.IWDFNamedPropertyStore~r1
title: IWDFNamedPropertyStore
author: windows-driver-content
description: The IWDFNamedPropertyStore interface exposes a property-store object.
old-location: wdf\iwdfnamedpropertystore.htm
old-project: wdf
ms.assetid: f31a88c1-468f-4756-a5fa-b4aa0b8fe51d
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
req.umdf-ver: 1.5
req.alt-api: IWDFNamedPropertyStore
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

# IWDFNamedPropertyStore interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFNamedPropertyStore</b> interface exposes a property-store object.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFNamedPropertyStore</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IWDFNamedPropertyStore</b> also has these types of members:

The <b>IWDFNamedPropertyStore</b> interface has these methods.

The <a href="wdf.iwdfnamedpropertystore_getnameat">GetNameAt</a> method retrieves the name of a property.

The <a href="wdf.iwdfnamedpropertystore_getnamecount">GetNameCount</a> method retrieves the number of properties in a property store.

The <a href="wdf.iwdfnamedpropertystore_getnamedvalue">GetNamedValue</a> method retrieves the value of a property.

The <a href="wdf.iwdfnamedpropertystore_setnamedvalue">SetNamedValue</a> method sets the value of a property.

 


## -members
The <b>IWDFNamedPropertyStore</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfnamedpropertystore_getnameat">IWDFNamedPropertyStore::GetNameAt</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfnamedpropertystore_getnameat">GetNameAt</a> method retrieves the name of a property.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfnamedpropertystore_getnamecount">IWDFNamedPropertyStore::GetNameCount</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfnamedpropertystore_getnamecount">GetNameCount</a> method retrieves the number of properties in a property store.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfnamedpropertystore_getnamedvalue">IWDFNamedPropertyStore::GetNamedValue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfnamedpropertystore_getnamedvalue">GetNamedValue</a> method retrieves the value of a property.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfnamedpropertystore_setnamedvalue">IWDFNamedPropertyStore::SetNamedValue</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfnamedpropertystore_setnamedvalue">SetNamedValue</a> method sets the value of a property.

</td>
</tr>
</table>The <a href="wdf.iwdfnamedpropertystore_getnameat">GetNameAt</a> method retrieves the name of a property.

The <a href="wdf.iwdfnamedpropertystore_getnamecount">GetNameCount</a> method retrieves the number of properties in a property store.

The <a href="wdf.iwdfnamedpropertystore_getnamedvalue">GetNamedValue</a> method retrieves the value of a property.

The <a href="wdf.iwdfnamedpropertystore_setnamedvalue">SetNamedValue</a> method sets the value of a property.

 


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
1.5

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