---
UID: NN:portcls.IRegistryKey
title: IRegistryKey
author: windows-driver-content
description: The IRegistryKey interface provides an abstraction of a registry key that a miniport driver can use to access the key and its subkeys.
old-location: audio\iregistrykey.htm
old-project: audio
ms.assetid: 41601234-7b8e-4d53-9455-626a5a3c4ff3
ms.author: windowsdriverdev
ms.date: 2/22/2018
ms.keywords: IRegistryKey, IRegistryKey interface [Audio Devices], IRegistryKey interface [Audio Devices], described, audio.iregistrykey, audmp-routines_40bea095-17f2-4b5f-96e8-ab2fed6d82d4.xml, portcls/IRegistryKey
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
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	portcls.h
api_name:
-	IRegistryKey
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IRegistryKey interface

The <code>IRegistryKey</code> interface provides an abstraction of a registry key that a miniport driver can use to access the key and its subkeys. The PortCls system driver implements this interface and exposes it to miniport drivers. A miniport driver obtains a reference to an <code>IRegistryKey</code> object by calling <a href="..\portcls\nf-portcls-pcnewregistrykey.md">PcNewRegistryKey</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff536945">IPort::NewRegistryKey</a>. 

For more information, see <a href="https://msdn.microsoft.com/c666f0cc-5a8a-4df8-9c65-08e3b044a08f">Registry Key Objects</a>.

## Methods

<p>The <b>IRegistryKey</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IRegistryKey::DeleteKey](nf-portcls-iregistrykey-deletekey.md) | The DeleteKey method deletes the registry key. |
| [IRegistryKey::EnumerateKey](nf-portcls-iregistrykey-enumeratekey.md) | The EnumerateKey method returns information about the subkeys of the open key. |
| [IRegistryKey::EnumerateValueKey](nf-portcls-iregistrykey-enumeratevaluekey.md) | The EnumerateValueKey method returns information about a registry entry that contains a value key. |
| [IRegistryKey::NewSubKey](nf-portcls-iregistrykey-newsubkey.md) | The NewSubKey method either creates a new registry subkey or opens an existing subkey under the key represented by the IRegistryKey object. |
| [IRegistryKey::QueryKey](nf-portcls-iregistrykey-querykey.md) | The QueryKey method retrieves information about a registry key, including the key name, key class, and the number of subkeys and their sizes. |
| [IRegistryKey::QueryRegistryValues](nf-portcls-iregistrykey-queryregistryvalues.md) | The QueryRegistryValues method allows the caller to query several values from the registry with a single call. |
| [IRegistryKey::QueryValueKey](nf-portcls-iregistrykey-queryvaluekey.md) | The QueryValueKey method retrieves information about a registry key's value entries, including their names, types, data sizes, and values. |
| [IRegistryKey::SetValueKey](nf-portcls-iregistrykey-setvaluekey.md) | The SetValueKey method replaces or creates a value entry under the open key. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | portcls.h |