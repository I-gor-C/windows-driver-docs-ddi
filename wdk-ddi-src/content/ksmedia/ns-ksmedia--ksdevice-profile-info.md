---
UID: NS.ksmedia._KSDEVICE_PROFILE_INFO
title: KSDEVICE_PROFILE_INFO
author: windows-driver-content
description: The KSDEVICE_PROFILE_INFO is a generic structure designed to handle profile information for various device types.
old-location: stream\ksdevice_profile_info.htm
ms.assetid: 32C894CA-B644-4221-97B6-A21F2A459DE6
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSDEVICE_PROFILE_INFO
req.alt-loc: ksmedia.h
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
ms.keywords: KSDEVICE_PROFILE_INFO, KSDEVICE_PROFILE_INFO, *PKSDEVICE_PROFILE_INFO
req.iface: 
---

# KSDEVICE_PROFILE_INFO structure



## -description
<p>The <b>KSDEVICE_PROFILE_INFO</b> is a generic structure designed to handle profile information for various device types.</p>


## -syntax

````
typedef struct _KSDEVICE_PROFILE_INFO {
  UINT32 Type;
  UINT32 Size;
  union {
    struct {
      KSCAMERA_PROFILE_INFO             Info;
      UINT32                            Reserved;
      UINT32                            ConcurrencyCount;
      PKSCAMERA_PROFILE_CONCURRENCYINFO Concurrency;
    } Camera;
  };
} KSDEVICE_PROFILE_INFO, *PKSDEVICE_PROFILE_INFO;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>Defines the type of profile. Currently, the only defined type is <b>KSDEVICE_PROFILE_TYPE_CAMERA</b>.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>#define KSDEVICE_PROFILE_TYPE_CAMERA    0x00000001</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>Size</b>

<dd>
<p>This must be set to sizeof(KSDEVICE_PROFILE_INFO) structure.</p>
</dd>

### -field <b>Camera</b>

<dd>
<dl>
<dd>
<p><b>Info</b></p>
<dl>
<dd>
<p>Structure of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925214">KSCAMERA_PROFILE_INFO</a> defining the profile information of a camera.</p>
</dd>
</dl>
</dd>
<dd>
<p><b>Reserved</b></p>
<dl>
<dd>
<p>Unused.  Must be set to 0.</p>
</dd>
</dl>
</dd>
<dd>
<p><b>ConcurrencyCount</b></p>
<dl>
<dd>
<p>Number of <a href="https://msdn.microsoft.com/library/windows/hardware/dn925213">KSCAMERA_PROFILE_CONCURRENCYINFO</a> structures in the <b>Concurrency</b> array.</p>
<p>For Windows 10 this must be less than or equal 1.</p>
<p>A value of 0 with <b>Concurrency</b> set to <b>NULL</b>, indicates this profile is non-concurrent.</p>
</dd>
</dl>
</dd>
<dd>
<p><b>Concurrency</b></p>
<dl>
<dd>
<p>An array of <b>KSCAMERA_PROFILE_CONCURRENCYINFO</b> structures describing the concurrency support for this profile.</p>
<p>If <b>CountOfConcurrency</b> is 0, this parameter must be <b>NULL</b>.</p>
<p>If <b>CountOfConcurrency</b> is greater than 0, this parameter must not be <b>NULL</b>.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>