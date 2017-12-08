---
UID: NN.wudfddi.IWDFPropertyStoreFactory~r1
title: IWDFPropertyStoreFactory
author: windows-driver-content
description: The IWDFPropertyStoreFactory interface is a factory interface that is used to create a property store interface.
old-location: wdf\iwdfpropertystorefactory.htm
old-project: wdf
ms.assetid: 41d77cf1-6f85-4f43-b2d8-1da4c9dac380
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: __MIDL___MIDL_itf_wudfddi_0000_0000_0001, *PPOWER_ACTION, POWER_ACTION
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
req.alt-api: IWDFPropertyStoreFactory
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

# IWDFPropertyStoreFactory interface



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]
The <b>IWDFPropertyStoreFactory</b> interface is a factory interface that is used to create a property store interface.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IWDFPropertyStoreFactory</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IWDFPropertyStoreFactory</b> also has these types of members:

The <b>IWDFPropertyStoreFactory</b> interface has these methods.

The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.

 

## -members
The <b>IWDFPropertyStoreFactory</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="wdf.iwdfpropertystorefactory_retrievedevicepropertystore">IWDFPropertyStoreFactory::RetrieveDevicePropertyStore</a>
</td>
<td align="left" width="63%">
The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.
</td>
</tr>
</table>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.

 

## -remarks
Drivers obtain the <b>IWDFPropertyStoreFactory</b> interface by calling <b>IWDFDevice::QueryInterface</b>,  <b>IWDFDeviceInitialize::QueryInterface</b> or <b>IWDFDeviceInitialize2::QueryInterface</b>.

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