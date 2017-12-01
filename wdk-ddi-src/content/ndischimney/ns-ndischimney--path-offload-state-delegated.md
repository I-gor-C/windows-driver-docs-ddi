---
UID: NS.ndischimney._PATH_OFFLOAD_STATE_DELEGATED
title: PATH_OFFLOAD_STATE_DELEGATED
author: windows-driver-content
description: The PATH_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a path state object.
old-location: netvista\path_offload_state_delegated.htm
old-project: netvista
ms.assetid: 3a1603ec-639f-4899-8889-3c7ed2cfe375
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PATH_OFFLOAD_STATE_DELEGATED, PATH_OFFLOAD_STATE_DELEGATED, *PPATH_OFFLOAD_STATE_DELEGATED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PATH_OFFLOAD_STATE_DELEGATED
req.alt-loc: ndischimney.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PATH_OFFLOAD_STATE_DELEGATED structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The PATH_OFFLOAD_STATE_DELEGATED structure contains the delegated variables of a path state
  object.</p>


## -syntax

````
typedef struct _PATH_OFFLOAD_STATE_DELEGATED {
  OFFLOAD_STATE_HEADER Header;
} PATH_OFFLOAD_STATE_DELEGATED, *PPATH_OFFLOAD_STATE_DELEGATED;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>An 
     <a href="..\ndischimney\ns-ndischimney--offload-state-header.md">OFFLOAD_STATE_HEADER</a> structure. NDIS
     sets the 
     <b>Length</b> member of 
     <b>Header</b> to the size, in bytes, of the PATH_OFFLOAD_STATE_DELEGATED structure. The 
     <b>RecognizedOptions</b> member of 
     <b>Header</b> is reserved.</p>
</dd>
</dl>

## -remarks
<p>Currently there are no delegated path variables.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\ns-ndischimney--offload-state-header.md">OFFLOAD_STATE_HEADER</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-cached.md">PATH_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-const.md">PATH_OFFLOAD_STATE_CONST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20PATH_OFFLOAD_STATE_DELEGATED structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
