---
UID: NE.storduid._DUID_MATCH_STATUS
title: DUID_MATCH_STATUS
author: windows-driver-content
description: The DUID_MATCH_STATUS enumeration lists the status values that the CompareStorageDuids routine returns.
old-location: storage\duid_match_status.htm
ms.assetid: 61a60e77-387c-42d6-b56b-694ce0c86570
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: storduid.h
req.include-header: Storduid.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DUID_MATCH_STATUS
req.alt-loc: storduid.h
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
ms.keywords: STI_USD_CAPS, STI_USD_CAPS, *PSTI_USD_CAPS
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# DUID_MATCH_STATUS enumeration



## -description
<p>The DUID_MATCH_STATUS enumeration lists the status values that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552464">CompareStorageDuids</a> routine returns.</p>


## -syntax

````
typedef enum _DUID_MATCH_STATUS { 
  DuidExactMatch                    = 0,
  DuidSubIdMatch                    = 1,
  DuidNoMatch                       = 2,
  DuidErrorGeneral                  = 100,
  DuidErrorMissingDuid              = 101,
  DuidErrorVersionMismatch          = 102,
  DuidErrorInvalidDuid              = 103,
  DuidErrorInvalidDeviceIdDescSize  = 104,
  DuidErrorInvalidDeviceDescSize    = 105,
  DuidErrorInvalidLayoutSigSize     = 106,
  DuidErrorInvalidLayoutSigVersion  = 107,
  DuidErrorMaximum                  = 108
} DUID_MATCH_STATUS;
````


## -enum-fields
<dl>

### -field <a id="DuidExactMatch"></a><a id="duidexactmatch"></a><a id="DUIDEXACTMATCH"></a><b>DuidExactMatch</b>

<dd>
<p>All fields in the two Device Unique Identifiers (DUIDs) match exactly.</p>
</dd>

### -field <a id="DuidSubIdMatch"></a><a id="duidsubidmatch"></a><a id="DUIDSUBIDMATCH"></a><b>DuidSubIdMatch</b>

<dd>
<p>Either the serial number or one of the unique sub-IDs matches. The two DUIDs probably represent the same device.</p>
</dd>

### -field <a id="DuidNoMatch"></a><a id="duidnomatch"></a><a id="DUIDNOMATCH"></a><b>DuidNoMatch</b>

<dd>
<p>None of the sub-IDs match in page 83h of the vital product data (VPD). None of the non-VPD data matches.</p>
</dd>

### -field <a id="DuidErrorGeneral"></a><a id="duiderrorgeneral"></a><a id="DUIDERRORGENERAL"></a><b>DuidErrorGeneral</b>

<dd>
<p>An error occurred for an unspecified cause.</p>
</dd>

### -field <a id="DuidErrorMissingDuid"></a><a id="duiderrormissingduid"></a><a id="DUIDERRORMISSINGDUID"></a><b>DuidErrorMissingDuid</b>

<dd>
<p>One of the two DUIDs to compare is missing.</p>
</dd>

### -field <a id="DuidErrorVersionMismatch"></a><a id="duiderrorversionmismatch"></a><a id="DUIDERRORVERSIONMISMATCH"></a><b>DuidErrorVersionMismatch</b>

<dd>
<p>The two DUIDs to compare do not have the same version.</p>
</dd>

### -field <a id="DuidErrorInvalidDuid"></a><a id="duiderrorinvalidduid"></a><a id="DUIDERRORINVALIDDUID"></a><b>DuidErrorInvalidDuid</b>

<dd>
<p>At least one of the two DUIDs to compare is invalid.</p>
</dd>

### -field <a id="DuidErrorInvalidDeviceIdDescSize"></a><a id="duiderrorinvaliddeviceiddescsize"></a><a id="DUIDERRORINVALIDDEVICEIDDESCSIZE"></a><b>DuidErrorInvalidDeviceIdDescSize</b>

<dd>
<p>At least one of the two DUIDs to compare contains an invalid device ID descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff566972">STORAGE_DEVICE_ID_DESCRIPTOR</a>). This descriptor reports VPD data.</p>
</dd>

### -field <a id="DuidErrorInvalidDeviceDescSize"></a><a id="duiderrorinvaliddevicedescsize"></a><a id="DUIDERRORINVALIDDEVICEDESCSIZE"></a><b>DuidErrorInvalidDeviceDescSize</b>

<dd>
<p>At least one of the two DUIDs to compare contains an invalid device descriptor (<a href="https://msdn.microsoft.com/library/windows/hardware/ff566971">STORAGE_DEVICE_DESCRIPTOR</a>). This descriptor reports non-VPD inquiry data..</p>
</dd>

### -field <a id="DuidErrorInvalidLayoutSigSize"></a><a id="duiderrorinvalidlayoutsigsize"></a><a id="DUIDERRORINVALIDLAYOUTSIGSIZE"></a><b>DuidErrorInvalidLayoutSigSize</b>

<dd>
<p>At least one of the two DUIDs to compare contains an invalid drive layout signature size.</p>
</dd>

### -field <a id="DuidErrorInvalidLayoutSigVersion"></a><a id="duiderrorinvalidlayoutsigversion"></a><a id="DUIDERRORINVALIDLAYOUTSIGVERSION"></a><b>DuidErrorInvalidLayoutSigVersion</b>

<dd>
<p>At least one of the two DUIDs to compare contains an invalid drive layout signature.</p>
</dd>

### -field <a id="DuidErrorMaximum"></a><a id="duiderrormaximum"></a><a id="DUIDERRORMAXIMUM"></a><b>DuidErrorMaximum</b>

<dd>
<p>This value delimits the upper limit of the enumeration values in this enumeration. This value allows a DUID consumer to create a loop that tests for all valid error values that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552464">CompareStorageDuids</a> routine returns. As new identifier data is added to future versions of the DUID, new error values will specify which parts of the DUID are not well-formed.</p>
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
<dt>Storduid.h (include Storduid.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552464">CompareStorageDuids</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566971">STORAGE_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566972">STORAGE_DEVICE_ID_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DUID_MATCH_STATUS enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
