---
UID: NF.wudfddi.IWDFDevice3.MapIoSpace
title: IWDFDevice3::MapIoSpace
author: windows-driver-content
description: The MapIoSpace method maps the given physical address range to system address space and returns a pseudo base address.
old-location: wdf\iwdfdevice3_mapiospace.htm
old-project: wdf
ms.assetid: 243C7299-7C74-408A-8FB9-32FB3315251F
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice3, MapIoSpace, IWDFDevice3::MapIoSpace
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
req.alt-api: IWDFDevice3.MapIoSpace
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
req.iface: IWDFDevice3
req.product: Windows 10 or later.
---

# IWDFDevice3::MapIoSpace method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>MapIoSpace</b> method maps the given physical address range to system address space and returns a pseudo base address. </p>


## -syntax

````
HRESULT  MapIoSpace(
  [in]  PHYSICAL_ADDRESS    PhysicalAddress,
  [in]  SIZE_T              NumberOfBytes,
  [in]  MEMORY_CACHING_TYPE CacheType,
  [out] VOID                **pPseudoBaseAddress
);
````


## -parameters
<dl>

### -param <i>PhysicalAddress</i> [in]

<dd>
<p>Specifies the starting 64-bit physical address of the I/O range to be mapped.</p>
</dd>

### -param <i>NumberOfBytes</i> [in]

<dd>
<p>Specifies a value greater than zero, indicating the number of bytes to be mapped.</p>
</dd>

### -param <i>CacheType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554430">MEMORY_CACHING_TYPE</a> value, which indicates the cache attribute to use to map the physical address range. The MEMORY_CACHING_TYPE enumeration type is defined in Wudfwdm.h.</p>
</dd>

### -param <i>pPseudoBaseAddress</i> [out]

<dd>
<p>The address of a location that receives a pointer to the pseudo base address.</p>
</dd>
</dl>

## -returns
<p>The method returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>A driver must call this method during device start-up if it receives translated resources of type <b>CmResourceTypeMemory</b> in a <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure. <b>MapIoSpace</b> maps the physical address returned in the resource list to a framework-managed address referred to as the pseudo base address.</p>

<p> The driver can then use the pseudo base address to access device registers with READ_REGISTER_<i>Xxx</i> and WRITE_REGISTER_<i>Xxx</i> functions. For  an example, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

<p>A driver that calls <b>MapIoSpace</b> must set the <b>UmdfDirectHardwareAccess</b> INF directive to <b>AllowDirectHardwareAccess</b>.</p>

<p> If the driver sets the <b>UmdfRegisterAccessMode</b> INF directive to <b>RegisterAccessUsingUserModeMapping</b>, calling <b>MapIoSpace</b> also maps the given physical address range to a user-mode base address range that the driver can subsequently access by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451219">GetHardwareRegisterMappedAddress</a>.</p>

<p> For more information about  INF directives that UMDF drivers can use, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.</p>

<p>The PHYSICAL_ADDRESS type is defined in Wudfwdm.h, as follows:<pre class="syntax" xml:space="preserve"><code>typedef LARGE_INTEGER PHYSICAL_ADDRESS;</code></pre>
</p>

<p>In the following code example, a UMDF driver uses its <a href="wdf.ipnpcallbackhardware2_onpreparehardware">IPnpCallbackHardware2::OnPrepareHardware</a> callback function to examine its memory-mapped register resources and map them into user-mode address space. The example then implements  a <b>WriteToDevice</b> method that accesses the memory locations. The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451237">UnmapIoSpace</a> from its <a href="wdf.ipnpcallbackhardware2_onreleasehardware">IPnpCallbackHardware2::OnReleaseHardware</a> callback. The driver’s INF file must enable UMDF hardware access feature by setting the <b>UmdfDirectHardwareAccess</b> directive to <b>AllowDirectHardwareAccess</b>.</p>

<p>A driver must call this method during device start-up if it receives translated resources of type <b>CmResourceTypeMemory</b> in a <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure. <b>MapIoSpace</b> maps the physical address returned in the resource list to a framework-managed address referred to as the pseudo base address.</p>

<p> The driver can then use the pseudo base address to access device registers with READ_REGISTER_<i>Xxx</i> and WRITE_REGISTER_<i>Xxx</i> functions. For  an example, see <a href="wdf.reading_and_writing_to_device_registers_in_umdf_1_x_drivers">Reading and Writing to Device Registers in UMDF 1.x Drivers</a>.</p>

<p>A driver that calls <b>MapIoSpace</b> must set the <b>UmdfDirectHardwareAccess</b> INF directive to <b>AllowDirectHardwareAccess</b>.</p>

<p> If the driver sets the <b>UmdfRegisterAccessMode</b> INF directive to <b>RegisterAccessUsingUserModeMapping</b>, calling <b>MapIoSpace</b> also maps the given physical address range to a user-mode base address range that the driver can subsequently access by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451219">GetHardwareRegisterMappedAddress</a>.</p>

<p> For more information about  INF directives that UMDF drivers can use, see <a href="wdf.specifying_wdf_directives_in_inf_files">Specifying WDF Directives in INF Files</a>.</p>

<p>The PHYSICAL_ADDRESS type is defined in Wudfwdm.h, as follows:<pre class="syntax" xml:space="preserve"><code>typedef LARGE_INTEGER PHYSICAL_ADDRESS;</code></pre>
</p>

<p>In the following code example, a UMDF driver uses its <a href="wdf.ipnpcallbackhardware2_onpreparehardware">IPnpCallbackHardware2::OnPrepareHardware</a> callback function to examine its memory-mapped register resources and map them into user-mode address space. The example then implements  a <b>WriteToDevice</b> method that accesses the memory locations. The driver then calls <a href="https://msdn.microsoft.com/library/windows/hardware/hh451237">UnmapIoSpace</a> from its <a href="wdf.ipnpcallbackhardware2_onreleasehardware">IPnpCallbackHardware2::OnReleaseHardware</a> callback. The driver’s INF file must enable UMDF hardware access feature by setting the <b>UmdfDirectHardwareAccess</b> directive to <b>AllowDirectHardwareAccess</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451197">IWDFDevice3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice3::MapIoSpace method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
