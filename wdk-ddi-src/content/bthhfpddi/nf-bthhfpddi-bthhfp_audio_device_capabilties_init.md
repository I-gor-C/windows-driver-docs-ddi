---
UID: NF.bthhfpddi.BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
title: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT function
author: windows-driver-content
description: The BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT method returns a pointer to an initialized BTHHFP_AUDIO_DEVICE_CAPABILTIES data structure.
old-location: audio\bthhfp_audio_device_capabilties_init.htm
old-project: audio
ms.assetid: c00b8f19-6708-4ec2-928b-610158850247
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: bthhfpddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT
req.alt-loc: bthhfpddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
---

# BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT function



## -description
The 
			
            <b>BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT</b> method returns a pointer to an initialized <a href="audio._bthhfp_audio_device_capabilties">BTHHFP_AUDIO_DEVICE_CAPABILTIES</a> data structure. 


## -syntax

````
FORCEINLINE VOID  BTHHFP_AUDIO_DEVICE_CAPABILTIES_INIT(
  _Out_ PBTHHFP_AUDIO_DEVICE_CAPABILTIES caps
);
````


## -parameters

### -param caps [out]

A pointer to an initialized <a href="audio._bthhfp_audio_device_capabilties">BTHHFP_AUDIO_DEVICE_CAPABILTIES</a> data structure.

## -returns
This method does not return a value.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 10
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2016
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Bthhfpddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
DISPATCH_LEVEL
</td>
</tr>
</table>