---
UID: NF.wudfddi.IWDFUnifiedPropertyStore.GetPropertyData
title: IWDFUnifiedPropertyStore::GetPropertyData
author: windows-driver-content
description: The GetPropertyData method retrieves the current setting for a device property.
old-location: wdf\iwdfunifiedpropertystore_getpropertydata.htm
old-project: wdf
ms.assetid: 0AAEB2F1-0449-4F0E-807A-1D2420CF6858
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFUnifiedPropertyStore, GetPropertyData, IWDFUnifiedPropertyStore::GetPropertyData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFUnifiedPropertyStore.GetPropertyData
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
req.iface: IWDFUnifiedPropertyStore
req.product: Windows 10 or later.
---

# IWDFUnifiedPropertyStore::GetPropertyData method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetPropertyData</b> method retrieves the current setting for a device property.
</p>


## -syntax

````
HRESULT GetPropertyData(
  [in]            const DEVPROPKEY  *PropertyKey,
  [in]                  LCID        Lcid,
  [in]                  ULONG       Flags,
  [in]                  ULONG       PropertyDataSize,
  [out, optional]       PVOID       PropertyData,
  [out]                 ULONG       *PropertyDataRequiredSize,
  [out]                 DEVPROPTYPE *PropertyType
);
````


## -parameters
<dl>

### -param PropertyKey [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> structure that specifies the device property key.</p>
</dd>

### -param Lcid [in]

<dd>
<p>Specifies a locale identifier. Set this parameter either to a language-specific LCID value or to LOCALE_NEUTRAL. The LOCALE_NEUTRAL LCID specifies that the property is language-neutral (that is, not specific to any language). Do not set this parameter to LOCALE_SYSTEM_DEFAULT or LOCALE_USER_DEFAULT. For more information about language-specific LCID values, see <a href="http://msdn.microsoft.com/en-us/library/cc233968(PROT.10).aspx">LCID Structure</a>.</p>
</dd>

### -param Flags [in]

<dd>
<p>Reserved for system use. Drivers should set this value to 0.</p>
</dd>

### -param PropertyDataSize [in]

<dd>
<p>The size, in bytes, of the buffer that <i>PropertyData</i> points to.</p>
</dd>

### -param PropertyData [out, optional]

<dd>
<p>A pointer to the device property data.</p>
</dd>

### -param PropertyDataRequiredSize [out]

<dd>
<p>A pointer to a ULONG to receive the size of the property information that is returned in <i>PropertyData</i>.</p>
</dd>

### -param PropertyType [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543546">DEVPROPTYPE</a> value. If <b>GetPropertyData</b> completes successfully, the method uses <i>PropertyType</i> to supply the type of data that is returned in the <i>PropertyData</i> buffer. </p>
</dd>
</dl>

## -returns
<p><b>GetPropertyData</b> returns S_OK if the operation succeeds. Otherwise, the method might return the following values.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>The framework's attempt to allocate memory failed.</p><dl>
<dt><b>HRESULT_FROM_NT(STATUS_BUFFER_TOO_SMALL)</b></dt>
</dl><p> The <i>PropertyDataRequiredSize</i> parameter contains the size of the required buffer.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (ERROR_INVALID_PARAMETER)</b></dt>
</dl><p>If the driver specifies <b>WdfPropertyStoreRootClassDeviceInterfaceKey</b>, the requested interface must be one that the UMDF driver previously registered.</p><dl>
<dt><b>HRESULT_FROM_WIN32 (STATUS_NOT_SUPPORTED)</b></dt>
</dl><p>The driver can request device interface property data only  starting with  Windows 8.</p>

<p> </p>

<p>This method might return one of the other values that <i>Winerror.h</i> contains.</p>

## -remarks
<p>Framework-based drivers use the <b>GetPropertyData</b> method to retrieve device properties that are defined as part of the unified device property model.</p>

<p>In particular, you can use this method to retrieve a device's <a href="wdf.using_the_registry_in_umdf_drivers">hardware key</a> or an instance of a device interface class. When you call <a href="wdf.iwdfunifiedpropertystorefactory_retrieveunifieddevicepropertystore">IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore</a>, set the <i>RootSpecifier</i> parameter's <b>RootClass</b> member to <b>WdfPropertyStoreRootClassHardwareKey</b> or <b>WdfPropertyStoreRootClassDeviceInterfaceKey</b>.</p>

<p>If you specify  <b>WdfPropertyStoreRootClassHardwareKey</b>, then when you call <b>GetPropertyData</b>, you must provide a custom <a href="https://msdn.microsoft.com/library/windows/hardware/dn315031">DEVPROPKEY</a> value in the <i>PropertyKey</i> parameter, and  not a PnP-defined key. The value must have been previously set by calling <a href="wdf.iwdfunifiedpropertystore_setpropertydata">SetPropertyData</a>, a <a href="devinst.using_device_installation_functions#ddk_setupdi_device_property_functions_dg#ddk_setupdi_device_property_functions_dg">SetupDI device property function</a>, or by using the <a href="devinst.using_the_inf_addproperty_directive_and_the_inf_delproperty_directive">INF AddProperty directive</a>.</p>

<p>For more information about device properties, see <a href="https://msdn.microsoft.com/f41040c5-0eac-450d-b532-9165c543cc1a">Device Properties</a>.</p>

<p>For more information about accessing the registry, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

<p>For variable size properties, the driver should make two passes to retrieve the property data. First, the driver should pass a NULL buffer in the <i>PropertyData</i> parameter, and set <i>PropertyDataSize</i> to 0.
Then, the driver should then allocate a buffer based on the <i>PropertyDataRequiredSize</i> returned and call <b>GetPropertyData</b> again, passing the allocated buffer.

The following example demonstrates this 
pattern.</p>

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

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfunifiedpropertystorefactory.md">IWDFUnifiedPropertyStoreFactory</a>
</dt>
<dt>
<a href="wdf.iwdfunifiedpropertystorefactory_retrieveunifieddevicepropertystore">RetrieveUnifiedDevicePropertyStore</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfunifiedpropertystore.md">IWDFUnifiedPropertyStore</a>
</dt>
<dt>
<a href="wdf.iwdfunifiedpropertystore_setpropertydata">SetPropertyData</a>
</dt>
<dt>
<a href="..\wudfddi_types\ns-wudfddi-types--wdf-property-store-root.md">WDF_PROPERTY_STORE_ROOT</a>
</dt>
<dt>
<a href="..\wudfddi_types\ne-wudfddi-types--wdf-property-store-root-class.md">WDF_PROPERTY_STORE_ROOT_CLASS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFUnifiedPropertyStore::GetPropertyData method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
