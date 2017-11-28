---
UID: NF.wudfddi.IWDFPropertyStoreFactory.RetrieveDevicePropertyStore
title: IWDFPropertyStoreFactory::RetrieveDevicePropertyStore
author: windows-driver-content
description: The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry.
old-location: wdf\iwdfpropertystorefactory_retrievedevicepropertystore.htm
old-project: wdf
ms.assetid: 23a4c968-b1d1-48f4-9ea9-b97c4b5b4208
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFPropertyStoreFactory, RetrieveDevicePropertyStore, IWDFPropertyStoreFactory::RetrieveDevicePropertyStore
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
req.alt-api: IWDFPropertyStoreFactory.RetrieveDevicePropertyStore
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
req.iface: IWDFPropertyStoreFactory
req.product: Windows 10 or later.
---

# IWDFPropertyStoreFactory::RetrieveDevicePropertyStore method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> method retrieves a property store interface that drivers can use to access the registry.</p>


## -syntax

````
HRESULT RetrieveDevicePropertyStore(
  [in]  PWDF_PROPERTY_STORE_ROOT          RootSpecifier,
  [in]  WDF_PROPERTY_STORE_RETRIEVE_FLAGS Flags,
  [in]  REGSAM                            DesiredAccess,
  [in]  PCWSTR                            SubkeyPath,
  [out] IWDFNamedPropertyStore2           **PropertyStore,
  [out] WDF_PROPERTY_STORE_DISPOSITION    *Disposition
);
````


## -parameters
<dl>

### -param <i>RootSpecifier</i> [in]

<dd>
<p>The address of a driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff561453">WDF_PROPERTY_STORE_ROOT</a> structure. The driver fills in this structure to identify the property store that <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> retrieves.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561449">WDF_PROPERTY_STORE_RETRIEVE_FLAGS</a>-typed flag that specifies whether UMDF should create a specified registry entry if it does not exist, and whether the new entry should be deleted when Windows restarts.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>A REGSAM-typed bit mask that specifies the types of access to the registry that you want your driver to have. The REGSAM type is defined in Winreg.h, and is described in the Windows SDK at <a href="http://go.microsoft.com/fwlink/p/?linkid=138045">REGSAM</a>. The bit mask must not specify GENERIC_WRITE, KEY_CREATE_SUB_KEY, or WRITE_DAC access. (Although the driver cannot specify KEY_CREATE_SUB_KEY, its call to <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> can create a subkey.)</p>
</dd>

### -param <i>SubkeyPath</i> [in]

<dd>
<p>A pointer to a caller-supplied character string that represents the name of a subkey located under the registry key that the <i>RootSpecifier</i> parameter specifies. This parameter is optional and can be <b>NULL</b>. See more information in Remarks.</p>
</dd>

### -param <i>PropertyStore</i> [out]

<dd>
<p>The address of a location that receives a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560168">IWDFNamedPropertyStore2</a> interface. The driver uses this interface to access values in the registry.</p>
</dd>

### -param <i>Disposition</i> [out]

<dd>
<p>The address of a location that receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561440">WDF_PROPERTY_STORE_DISPOSITION</a>-typed value. </p>
</dd>
</dl>

## -returns
<p>
<a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> returns S_OK if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The caller provided an invalid input argument.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p>An attempt to allocate memory failed.</p>

<p> </p>

<p>This method might return one of the other values that Winerror.h contains

</p>

## -remarks
<p>Your driver can call <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> to obtain access to the driver's software key, the current device's hardware key, keys for the device interfaces that the current device supports, or the <b>DEVICEMAP</b> key.</p>

<p>If you supply the <i>SubkeyPath</i> parameter, you must use a unique name, such as the driver's service name. A driver might use a subkey to store device-specific information.</p>

<p>For more information about using <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> to access the registry, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>. </p>

<p>The following code example retrieves the value that is assigned to the <b>PortName</b> entry under a device's hardware key.</p>

<p>Your driver can call <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> to obtain access to the driver's software key, the current device's hardware key, keys for the device interfaces that the current device supports, or the <b>DEVICEMAP</b> key.</p>

<p>If you supply the <i>SubkeyPath</i> parameter, you must use a unique name, such as the driver's service name. A driver might use a subkey to store device-specific information.</p>

<p>For more information about using <a href="wdf.iwdfdevice_retrievedevicepropertystore">RetrieveDevicePropertyStore</a> to access the registry, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>. </p>

<p>The following code example retrieves the value that is assigned to the <b>PortName</b> entry under a device's hardware key.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560223">IWDFPropertyStoreFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558842">IWDFDevice::RetrieveDevicePropertyStore</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556982">IWDFDeviceInitialize::RetrieveDevicePropertyStore</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFPropertyStoreFactory::RetrieveDevicePropertyStore method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
