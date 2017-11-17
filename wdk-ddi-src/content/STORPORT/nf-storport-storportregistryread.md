---
UID: NF.storport.StorPortRegistryRead
title: StorPortRegistryRead
author: windows-driver-content
description: The StorPortRegistryRead routine reads the registry data for the indicated device and value.
old-location: storage\storportregistryread.htm
ms.assetid: 16f13973-c1c1-4123-8fa4-20187ec2c204
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortRegistryRead
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: StorPortIrql
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: StorPortRegistryRead
req.iface: 
req.product: Windows 10 or later.
---

# StorPortRegistryRead function



## -description
<p>The <b>StorPortRegistryRead</b> routine reads the registry data for the indicated device and value. </p>


## -syntax

````
BOOLEAN StorPortRegistryRead(
   IN PVOID  HwDeviceExtension,
   IN PUCHAR ValueName,
   IN ULONG  Global,
   IN ULONG  Type,
   IN PUCHAR Buffer,
   IN PULONG BufferLength
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff567108">StorPortInitialize</a>. The port driver frees this memory when it removes the device. The miniport driver must be running at IRQL PASSIVE_LEVEL when it calls this routine.</p>
</dd>

### -param <i>ValueName</i> 

<dd>
<p>Pointer to a UCHAR that specifies the registry value name whose content is to be read. </p>
</dd>

### -param <i>Global</i> 

<dd>
<p>Indicates, when nonzero, that the port driver reads the contents of the registry value specified by <i>ValueName</i> under the Parameters\Device subkey. The values under the Device key apply to all adapters in the system. When <i>Global</i> is zero, the port driver reads the contents of the registry value specified by <i>ValueName</i> under the Parameters\Device(d) subkey, where (d) is a decimal value that corresponds to the port number of a particular adapter. In this case, the data retrieved is adapter-specific. </p>
</dd>

### -param <i>Type</i> 

<dd>
<p>Indicates the data type of registry value. This parameter must have one of the values in the following table.</p>
<table>
<tr>
<th>Registry value data type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>REG_NONE</p>
</td>
<td>
<p>No data type specified. </p>
</td>
</tr>
<tr>
<td>
<p>REG_SZ</p>
</td>
<td>
<p>Indicates a <b>NULL</b>-terminated Unicode string.</p>
</td>
</tr>
<tr>
<td>
<p>REG_EXPAND_SZ</p>
</td>
<td>
<p>Indicates a <b>NULL</b>-terminated Unicode string that includes environment variables that must be expanded to obtain the complete string. For example, a path name might be stored as the following string: "%USERPROFILE%\Application Data ".</p>
<p>In this example, the environment variable USERPROFILE must be expanded to obtain the actual pathname.</p>
</td>
</tr>
<tr>
<td>
<p>REG_BINARY</p>
</td>
<td>
<p>Indicates a raw binary data.</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD</p>
</td>
<td>
<p>Indicates a 32-bit double word value.</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD_LITTLE_ENDIAN</p>
</td>
<td>
<p>Indicates a 32-bit double word value, in little-endian order. This is identical to REG_DWORD.</p>
</td>
</tr>
<tr>
<td>
<p>REG_DWORD_BIG_ENDIAN</p>
</td>
<td>
<p>Indicates a 32-bit double word value, in big-endian order. </p>
</td>
</tr>
<tr>
<td>
<p>REG_LINK</p>
</td>
<td>
<p>Indicates a Unicode string containing a symbolic link. </p>
</td>
</tr>
<tr>
<td>
<p>REG_MULTI_SZ</p>
</td>
<td>
<p>Indicates a series of <b>NULL</b>-terminated strings.</p>
</td>
</tr>
<tr>
<td>
<p>REG_RESOURCE_LIST</p>
</td>
<td>
<p>Indicates that the registry value contains a list of hardware resources, also known as the "hardware resource map", that is stored under the HKEY_LOCAL_MACHINE\HARDWARE\ResourceMap hive.</p>
</td>
</tr>
<tr>
<td>
<p>REG_FULL_RESOURCE_DESCRIPTOR</p>
</td>
<td>
<p>Indicates that the registry value contains a description of hardware resources stored under the HKEY_LOCAL_MACHINE\HARDWARE\Description hive.</p>
</td>
</tr>
<tr>
<td>
<p>REG_RESOURCE_REQUIREMENTS_LIST</p>
</td>
<td>
<p>Indicates that the registry value contains a list of hardware resource requirements stored under the HKEY_LOCAL_MACHINE\HARDWARE\ResourceMap tree.</p>
</td>
</tr>
<tr>
<td>
<p>REG_QWORD</p>
</td>
<td>
<p>Indicates that the registry value contains a 64-bit number.</p>
</td>
</tr>
<tr>
<td>
<p>REG_QWORD_LITTLE_ENDIAN</p>
</td>
<td>
<p>Indicates that the registry value contains a 64-bit number. This is the same data type as REG_QWORD. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Buffer</i> 

<dd>
<p>Pointer to the buffer where the retrieved registry information is to be reported. </p>
</dd>

### -param <i>BufferLength</i> 

<dd>
<p>Pointer to a ULONG that contains the size, in bytes, of the registry data returned. </p>
</dd>
</dl>

## -returns
<p><b>StorPortRegistryRead</b> returns a Boolean value of <b>TRUE</b> if the data pointed to by <i>ValueName</i> is successfully converted into ASCII and copied into the buffer. This routine returns <b>FALSE</b> in the event of an error. </p>

## -remarks
<p>If <b>StorPortRegistryRead</b> returns <b>FALSE</b> with a nonzero value in the <i>BufferLength</i> parameter, the buffer that was passed was too small and the <i>BufferLength</i> parameter reflects the correct buffer size that should be used. If the routine returns <b>FALSE</b> with the <i>BufferLength</i> parameter set to zero, another error has occurred.</p>

<p>The buffer used in this routine is allocated by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567034">StorPortAllocateRegistryBuffer</a> and freed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567067">StorPortFreeRegistryBuffer</a>.</p>

<p>If <b>StorPortRegistryRead</b> returns <b>FALSE</b> with a nonzero value in the <i>BufferLength</i> parameter, the buffer that was passed was too small and the <i>BufferLength</i> parameter reflects the correct buffer size that should be used. If the routine returns <b>FALSE</b> with the <i>BufferLength</i> parameter set to zero, another error has occurred.</p>

<p>The buffer used in this routine is allocated by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567034">StorPortAllocateRegistryBuffer</a> and freed by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567067">StorPortFreeRegistryBuffer</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454266">StorPortIrql</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567034">StorPortAllocateRegistryBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567067">StorPortFreeRegistryBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortRegistryRead routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
