---
UID : NE:wdm._IMAGE_POLICY_ID
title : _IMAGE_POLICY_ID
author : windows-driver-content
description : This enumeration is not supported.
old-location : kernel\_image_policy_id.htm
old-project : kernel
ms.assetid : e2984ef0-6648-41d3-89da-4f57cce66cfb
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _IMAGE_POLICY_ID, IMAGE_POLICY_ID
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : wdm.h
req.include-header : Wdm.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IMAGE_POLICY_ID
req.alt-loc : wdm.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : IMAGE_POLICY_ID
req.product : Windows 10 or later.
---

# _IMAGE_POLICY_ID Enumeration
This enumeration is not supported.

## Syntax
````
typedef enum _IMAGE_POLICY_ID { 
  ImagePolicyIdEtw,
  ImagePolicyIdDebug,
  ImagePolicyIdCrashDump,
  ImagePolicyIdCrashDumpKey,
  ImagePolicyIdCrashDumpKeyGuid,
  ImagePolicyIdParentSd,
  ImagePolicyIdParentSdRev,
  ImagePolicyIdSvn,
  ImagePolicyIdDeviceId,
  ImagePolicyIdCapability,
  ImagePolicyIdScenarioId,
  ImagePolicyIdMaximum
} IMAGE_POLICY_ID;
````

## Constants

<table>

<tr>
<td>ImagePolicyIdCapability</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdCrashDump</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdCrashDumpKey</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdCrashDumpKeyGuid</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdDebug</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdDeviceId</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdEtw</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdMaximum</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdParentSd</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdParentSdRev</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdScenarioId</td>
<td>Reserved.</td>
</tr>

<tr>
<td>ImagePolicyIdSvn</td>
<td>Reserved.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h) |