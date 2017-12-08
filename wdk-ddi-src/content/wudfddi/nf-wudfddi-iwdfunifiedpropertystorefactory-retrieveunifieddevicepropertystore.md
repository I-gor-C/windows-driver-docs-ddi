---
UID: NF.wudfddi.IWDFUnifiedPropertyStoreFactory.RetrieveUnifiedDevicePropertyStore
title: IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore
author: windows-driver-content
description: The RetrieveUnifiedDevicePropertyStore method retrieves a unified property store interface.
old-location: wdf\iwdfunifiedpropertystorefactory_retrieveunifieddevicepropertystore.htm
old-project: wdf
ms.assetid: A54E56A6-9A6C-435D-83FD-84BB0E072C74
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFUnifiedPropertyStoreFactory, RetrieveUnifiedDevicePropertyStore, IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFUnifiedPropertyStoreFactory.RetrieveUnifiedDevicePropertyStore
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
req.iface: IWDFUnifiedPropertyStoreFactory
req.product: Windows 10 or later.
---

# IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>RetrieveUnifiedDevicePropertyStore</b> method retrieves a unified property store interface.</p>


## -syntax

````
HRESULT RetrieveUnifiedDevicePropertyStore(
  [in]  PWDF_PROPERTY_STORE_ROOT RootSpecifier,
  [out] IWDFUnifiedPropertyStore **PropertyStore
);
````


## -parameters
<dl>

### -param RootSpecifier [in]

<dd>
<p>The address of a driver-allocated <a href="..\wudfddi_types\ns-wudfddi-types--wdf-property-store-root.md">WDF_PROPERTY_STORE_ROOT</a> structure. The driver fills in this structure to identify the unified property store that <b>RetrieveUnifiedDevicePropertyStore</b> retrieves.</p>
</dd>

### -param PropertyStore [out]

<dd>
<p>The address of a location that receives a pointer to an <a href="..\wudfddi\nn-wudfddi-iwdfunifiedpropertystore.md">IWDFUnifiedPropertyStore</a> interface.</p>
</dd>
</dl>

## -returns
<p><b>RetrieveUnifiedDevicePropertyStore</b> returns S_OK if the operation succeeds. Otherwise, the method might return one of the following values.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The caller provided an invalid input argument.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>An attempt to allocate memory failed.</p>

<p> </p>

<p>This method might return one of the other values that <i>Winerror.h</i> contains.</p>

## -remarks
<p>Your driver can call <b>RetrieveUnifiedDevicePropertyStore</b> to obtain access to a current device's hardware key or a device interface key that the device supports.</p>

<p>The <b>RootClass</b> member of the <a href="..\wudfddi_types\ns-wudfddi-types--wdf-property-store-root.md">WDF_PROPERTY_STORE_ROOT</a> structure pointed to by <i>RootSpecifier</i> must be set to <b>WdfPropertyStoreRootClassHardwareKey</b> or <b>WdfPropertyStoreRootClassDeviceInterfaceKey</b>.</p>

<p>In addition, if <b>RootClass</b> is set to <b>WdfPropertyStoreRootClassHardwareKey</b>, then the <b>Qualifier.HardwareKey.ServiceName</b> member of <i>RootSpecifier</i> must be NULL.</p>

<p>For more information about accessing the registry, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

<p>The following code example retrieves a unified property store interface.</p>

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
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfunifiedpropertystorefactory.md">IWDFUnifiedPropertyStoreFactory</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfunifiedpropertystore.md">IWDFUnifiedPropertyStore</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
