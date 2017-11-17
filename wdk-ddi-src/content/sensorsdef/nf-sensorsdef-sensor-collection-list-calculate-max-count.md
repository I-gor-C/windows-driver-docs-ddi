---
UID: NF.sensorsdef.SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT
title: SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT
author: windows-driver-content
description: This function calculates the number of SENSOR_VALUE_PAIR elements in a SENSOR_COLLECTION_LIST structure.
old-location: sensors\sensor_collection_list_calculate_max_count.htm
ms.assetid: 56C94717-41FF-44AA-BC99-1ECE4A407A38
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: sensors
req.header: sensorsdef.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT
req.alt-loc: Sensorsdef.h
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
ms.keywords: SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT
req.iface: 
req.product: Windows 10 or later.
---

# SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT function



## -description
<p>This function calculates the number of <a href="https://msdn.microsoft.com/library/windows/hardware/dn946708">SENSOR_VALUE_PAIR</a> elements in a <a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a> structure.</p>


## -syntax

````
FORCEINLINE ULONG SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT(
  _In_ PSENSOR_COLLECTION_LIST pCollectionList
);
````


## -parameters
<dl>

### -param <i>pCollectionList</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a> structure.</p>
</dd>
</dl>

## -returns
<p>The <b>SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT</b> function returns a ULONG value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorsdef.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn957092">SENSOR_COLLECTION_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946708">SENSOR_VALUE_PAIR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20SENSOR_COLLECTION_LIST_CALCULATE_MAX_COUNT function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
