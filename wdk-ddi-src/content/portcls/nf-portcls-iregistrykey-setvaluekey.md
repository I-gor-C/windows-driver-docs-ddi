---
UID: NF.portcls.IRegistryKey.SetValueKey
title: IRegistryKey::SetValueKey
author: windows-driver-content
description: The SetValueKey method replaces or creates a value entry under the open key.
old-location: audio\iregistrykey_setvaluekey.htm
old-project: audio
ms.assetid: 4f9dd025-b49f-44ab-88c4-38139e6cbee2
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IRegistryKey, SetValueKey, IRegistryKey::SetValueKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRegistryKey.SetValueKey
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
req.iface: IRegistryKey
---

# IRegistryKey::SetValueKey method



## -description
<p>The <code>SetValueKey</code> method replaces or creates a value entry under the open key.</p>


## -syntax

````
NTSTATUS SetValueKey(
  [in, optional] PUNICODE_STRING ValueName,
  [in]           ULONG           Type,
  [in]           PVOID           Data,
  [in]           ULONG           DataSize
);
````


## -parameters
<dl>

### -param <i>ValueName</i> [in, optional]

<dd>
<p>Pointer to a string containing the name of the value entry to set. The name string is specified by a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>. If the value entry has no name, set this parameter to <b>NULL</b>. If the caller specifies a name string but the given name is not unique relative to its containing key, the method replaces the data for an existing value entry.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>Specifies the type of the data to be written for <i>ValueName</i>. Set this parameter to one of the following system-defined types:</p>
<dl>
<dd>
<p>REG_BINARY</p>
</dd>
<dd>
<p>REG_DWORD</p>
</dd>
<dd>
<p>REG_DWORD_LITTLE_ENDIAN</p>
</dd>
<dd>
<p>REG_DWORD_BIG_ENDIAN</p>
</dd>
<dd>
<p>REG_EXPAND_SZ</p>
</dd>
<dd>
<p>REG_LINK</p>
</dd>
<dd>
<p>REG_MULTI_SZ</p>
</dd>
<dd>
<p>REG_NONE</p>
</dd>
<dd>
<p>REG_SZ</p>
</dd>
<dd>
<p>REG_RESOURCE_LIST</p>
</dd>
<dd>
<p>REG_RESOURCE_REQUIREMENTS_LIST</p>
</dd>
<dd>
<p>REG_FULL_RESOURCE_DESCRIPTOR</p>
</dd>
</dl>
<p>These parameter types are explained in <a href="https://msdn.microsoft.com/library/windows/hardware/ff567109">ZwSetValueKey</a>.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>Pointer to a buffer containing the data. This parameter points to a user-supplied structure or value appropriate to the function.</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>Specifies the size in bytes of <i>Data</i>. This parameter specifies how many bytes of data the method will copy from the buffer that <i>Data</i> points to.</p>
</dd>
</dl>

## -returns
<p><code>SetValueKey</code> returns STATUS_SUCCESS if the call was successful in setting the specified value key. Otherwise, the method returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that one of the parameters passed to the method is not valid.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>Indicates that method was unable to find the named value key.</p>

<p> </p>

## -remarks
<p>If the given key has no existing value entry with a name matching the given <i>ValueName</i>, <code>SetValueKey</code> creates a new value entry with the given name. If a matching value entry name exists, this routine overwrites the original value entry for the given <i>ValueName</i>. Thus, <code>SetValueKey</code> preserves a unique name for each value entry of any particular key. While each value entry name must be unique to its containing key, many different keys in the registry can have value entries with the same names.</p>

<p>If the given key has no existing value entry with a name matching the given <i>ValueName</i>, <code>SetValueKey</code> creates a new value entry with the given name. If a matching value entry name exists, this routine overwrites the original value entry for the given <i>ValueName</i>. Thus, <code>SetValueKey</code> preserves a unique name for each value entry of any particular key. While each value entry name must be unique to its containing key, many different keys in the registry can have value entries with the same names.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536965">IRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567109">ZwSetValueKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IRegistryKey::SetValueKey method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
