---
UID: NN.portcls.IRegistryKey
title: IRegistryKey
author: windows-driver-content
description: The IRegistryKey interface provides an abstraction of a registry key that a miniport driver can use to access the key and its subkeys.
old-location: audio\iregistrykey.htm
old-project: audio
ms.assetid: 41601234-7b8e-4d53-9455-626a5a3c4ff3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterIoTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRegistryKey
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
req.iface: 
---

# IRegistryKey interface



## -description
<p>The <code>IRegistryKey</code> interface provides an abstraction of a registry key that a miniport driver can use to access the key and its subkeys. The PortCls system driver implements this interface and exposes it to miniport drivers. A miniport driver obtains a reference to an <code>IRegistryKey</code> object by calling <a href="..\portcls\nf-portcls-pcnewregistrykey.md">PcNewRegistryKey</a> or <a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a>. </p>
<p>For more information, see <a href="https://msdn.microsoft.com/c666f0cc-5a8a-4df8-9c65-08e3b044a08f">Registry Key Objects</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IRegistryKey</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IRegistryKey</b> also has these types of members:</p>

<p>The <b>IRegistryKey</b> interface has these methods.</p>

<p>The <code>DeleteKey</code> method deletes the registry key.</p>

<p>The <code>EnumerateKey</code> method returns information about the subkeys of the open key.</p>

<p>The <code>EnumerateValueKey</code> method returns information about a registry entry that contains a value key.</p>

<p>The <code>NewSubKey</code> method either creates a new registry subkey or opens an existing subkey under the key represented by the <b>IRegistryKey</b> object.</p>

<p>The <code>QueryKey</code> method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes.</p>

<p>The <code>QueryRegistryValues</code> method allows the caller to query several values from the registry with a single call.</p>

<p>The <code>QueryValueKey</code> method retrieves information about a registry key's value entries, including their names, types, data sizes, and values.</p>

<p>The <code>SetValueKey</code> method replaces or creates a value entry under the open key.</p>

<p> </p>

## -members
<p>The <b>IRegistryKey</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_deletekey">IRegistryKey::DeleteKey</a>
</td>
<td align="left" width="63%">
<p>The <code>DeleteKey</code> method deletes the registry key.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_enumeratekey">IRegistryKey::EnumerateKey</a>
</td>
<td align="left" width="63%">
<p>The <code>EnumerateKey</code> method returns information about the subkeys of the open key.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_enumeratevaluekey">IRegistryKey::EnumerateValueKey</a>
</td>
<td align="left" width="63%">
<p>The <code>EnumerateValueKey</code> method returns information about a registry entry that contains a value key.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_newsubkey">IRegistryKey::NewSubKey</a>
</td>
<td align="left" width="63%">
<p>The <code>NewSubKey</code> method either creates a new registry subkey or opens an existing subkey under the key represented by the <b>IRegistryKey</b> object.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_querykey">IRegistryKey::QueryKey</a>
</td>
<td align="left" width="63%">
<p>The <code>QueryKey</code> method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_queryregistryvalues">IRegistryKey::QueryRegistryValues</a>
</td>
<td align="left" width="63%">
<p>The <code>QueryRegistryValues</code> method allows the caller to query several values from the registry with a single call.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_queryvaluekey">IRegistryKey::QueryValueKey</a>
</td>
<td align="left" width="63%">
<p>The <code>QueryValueKey</code> method retrieves information about a registry key's value entries, including their names, types, data sizes, and values.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="audio.iregistrykey_setvaluekey">IRegistryKey::SetValueKey</a>
</td>
<td align="left" width="63%">
<p>The <code>SetValueKey</code> method replaces or creates a value entry under the open key.</p>
</td>
</tr>
</table><p>The <code>DeleteKey</code> method deletes the registry key.</p>

<p>The <code>EnumerateKey</code> method returns information about the subkeys of the open key.</p>

<p>The <code>EnumerateValueKey</code> method returns information about a registry entry that contains a value key.</p>

<p>The <code>NewSubKey</code> method either creates a new registry subkey or opens an existing subkey under the key represented by the <b>IRegistryKey</b> object.</p>

<p>The <code>QueryKey</code> method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes.</p>

<p>The <code>QueryRegistryValues</code> method allows the caller to query several values from the registry with a single call.</p>

<p>The <code>QueryValueKey</code> method retrieves information about a registry key's value entries, including their names, types, data sizes, and values.</p>

<p>The <code>SetValueKey</code> method replaces or creates a value entry under the open key.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>