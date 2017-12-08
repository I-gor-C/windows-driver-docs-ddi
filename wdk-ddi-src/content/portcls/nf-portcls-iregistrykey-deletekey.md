---
UID: NF.portcls.IRegistryKey.DeleteKey
title: IRegistryKey::DeleteKey
author: windows-driver-content
description: The DeleteKey method deletes the registry key.
old-location: audio\iregistrykey_deletekey.htm
old-project: audio
ms.assetid: 2930b049-7572-4ee5-bef1-fd4485e5f644
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IRegistryKey, DeleteKey, IRegistryKey::DeleteKey
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
req.alt-api: IRegistryKey.DeleteKey
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

# IRegistryKey::DeleteKey method



## -description
<p>The <code>DeleteKey</code> method deletes the registry key.</p>


## -syntax

````
NTSTATUS DeleteKey(
    None
);
````


## -parameters
<dl>

### -param None 

<dd></dd>
</dl>

## -returns
<p><code>DeleteKey</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code.</p>

## -remarks
<p>A caller deletes an <b>IRegistryKey</b> object's registry key by calling the <code>DeleteKey</code> method on that object. The key can be deleted only if the caller created the key with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> that permits deletion. The caller enables deletion by specifying a <i>DesiredAccess</i> parameter value of KEY_ALL_ACCESS (described in <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>) to the <a href="..\portcls\nf-portcls-pcnewregistrykey.md">PcNewRegistryKey</a>, <a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a>, or <a href="audio.iregistrykey_newsubkey">IRegistryKey::NewSubKey</a> call that creates the key. When deleting a key, the <b>IRegistryKey</b> object discards its registry-key handle, and all other handles to the deleted key become invalid.</p>

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
<a href="..\portcls\nn-portcls-iregistrykey.md">IRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwdeletekey.md">ZwDeleteKey</a>
</dt>
<dt>
<a href="..\portcls\nf-portcls-pcnewregistrykey.md">PcNewRegistryKey</a>
</dt>
<dt>
<a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a>
</dt>
<dt>
<a href="audio.iregistrykey_newsubkey">IRegistryKey::NewSubKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IRegistryKey::DeleteKey method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
