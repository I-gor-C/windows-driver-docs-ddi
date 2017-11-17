---
UID: NF.portcls.IRegistryKey.EnumerateValueKey
title: IRegistryKey::EnumerateValueKey
author: windows-driver-content
description: The EnumerateValueKey method returns information about a registry entry that contains a value key.
old-location: audio\iregistrykey_enumeratevaluekey.htm
ms.assetid: 4f90b553-f652-413f-9723-a5a578de9f8d
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRegistryKey.EnumerateValueKey
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: IRegistryKey, EnumerateValueKey, IRegistryKey::EnumerateValueKey
req.iface: IRegistryKey
---

# IRegistryKey::EnumerateValueKey method



## -description
<p>The <code>EnumerateValueKey</code> method returns information about a registry entry that contains a value key.</p>


## -syntax

````
NTSTATUS EnumerateValueKey(
  [in]  ULONG                       Index,
  [in]  KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
  [out] PVOID                       KeyValueInformation,
  [in]  ULONG                       Length,
  [out] PULONG                      ResultLength
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the subkey index. This parameter identifies the subkey whose value is requested. If the key contains <i>n</i> subkeys, valid indices range from 0 to <i>n</i>-1. If the index exceeds this range, the method returns STATUS_NO_MORE_ENTRIES.</p>
</dd>

### -param <i>KeyValueInformationClass</i> [in]

<dd>
<p>Specifies the type of information to be returned in the buffer. Set this parameter to one of the following KEY_VALUE_INFORMATION_CLASS enumeration values:</p>
<ul>
<li>
<p><b>KeyValueBasicInformation</b></p>
</li>
<li>
<p><code>KeyValueFullInformation</code></p>
</li>
<li>
<p><code>KeyValuePartialInformation</code></p>
</li>
</ul>
</dd>

### -param <i>KeyValueInformation</i> [out]

<dd>
<p>Output pointer for the key value. This parameter points to a caller-allocated buffer into which the method writes the requested data. The buffer contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff553410">KEY_VALUE_BASIC_INFORMATION</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554217">KEY_VALUE_FULL_INFORMATION</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554220">KEY_VALUE_PARTIAL_INFORMATION</a>, depending on the value of <i>KeyValueInformationClass</i>. The structure is followed by additional data whose size depends on the data type of the key value.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Size in bytes of the <i>KeyValueInformation</i> buffer, which the caller must set according to the given <i>KeyValueInformationClass</i>. For the call to succeed, the buffer must be at least as large as the data that the method writes into the buffer.</p>
</dd>

### -param <i>ResultLength</i> [out]

<dd>
<p>Output pointer for the length of the resulting data. This parameter points to a caller-allocated ULONG variable into which the method writes a count specifying the number of bytes actually written into the <i>KeyValueInformation</i> buffer. If the specified buffer length is too small to contain the information, however, the method instead outputs the required buffer size and returns STATUS_BUFFER_OVERFLOW.</p>
</dd>
</dl>

## -returns
<p><code>EnumerateValueKey</code> returns STATUS_SUCCESS if the call was successful in copying the requested information into the <i>KeyValueInformation</i> buffer. If the specified buffer size is too small to receive all of the available information, the method returns STATUS_BUFFER_OVERFLOW. Otherwise, the method returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>Indicates that the specified buffer is too small to receive any information.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameters passed to the method is not valid.</p><dl>
<dt><b>STATUS_NO_MORE_ENTRIES</b></dt>
</dl><p>Indicates that no more value keys are available (the <i>Index</i> parameter is greater than or equal to the number of value keys).</p>

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
<dt>Portcls.h (include Portcls.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553410">KEY_VALUE_BASIC_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554217">KEY_VALUE_FULL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554220">KEY_VALUE_PARTIAL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566453">ZwEnumerateValueKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IRegistryKey::EnumerateValueKey method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
