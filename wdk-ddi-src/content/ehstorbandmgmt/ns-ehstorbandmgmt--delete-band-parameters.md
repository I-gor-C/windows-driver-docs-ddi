---
UID: NS.ehstorbandmgmt._DELETE_BAND_PARAMETERS
title: DELETE_BAND_PARAMETERS
author: windows-driver-content
description: A configured band is deleted according to the parameters in a DELETE_BAND_PARAMETERS structure. This structure is input for an IOCTL_EHSTOR_BANDMGMT_DELETE_BAND request.
old-location: storage\delete_band_parameters.htm
old-project: storage
ms.assetid: 6C96CF49-A7B2-4A99-8C7A-FC1C8C389C18
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DELETE_BAND_PARAMETERS, DELETE_BAND_PARAMETERS, *PDELETE_BAND_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ehstorbandmgmt.h
req.include-header: EhStorBandMgmt.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DELETE_BAND_PARAMETERS
req.alt-loc: EhStorBandMgmt.h
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

# DELETE_BAND_PARAMETERS structure



## -description
<p>A configured band is deleted according to the parameters in a <b>DELETE_BAND_PARAMETERS</b> structure. This structure is input for an <a href="..\ehstorbandmgmt\ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-delete-band.md"> IOCTL_EHSTOR_BANDMGMT_DELETE_BAND</a> request.</p>


## -syntax

````
typedef struct _DELETE_BAND_PARAMETERS {
  ULONG         StructSize;
  ULONG         Flags;
  ULONG         Reserved;
  ULONG         BandId;
  LARGE_INTEGER BandStart;
  ULONG         AuthKeyOffset;
} DELETE_BAND_PARAMETERS, *PDELETE_BAND_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>StructSize</b>

<dd>
<p>The size of this structure in bytes. Set to <b>sizeof</b>(DELETE_BAND_PARAMETERS).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Delete operation flags. This value is a bitwise OR combination of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="DELBAND_ERASE_BEFORE_DELETE"></a><a id="delband_erase_before_delete"></a><dl>

### -field <b>DELBAND_ERASE_BEFORE_DELETE</b>

</dl>
</td>
<td width="60%">
<p>Perform a cryptographic erase of the band property data before delete.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>BandId</b>

<dd>
<p>The identifier of a single band to return information for. <b>BandSize</b> must be 0 when a single band is selected  with <b>BandId</b>. To use <b>BandStart</b> and <b>BandSize</b> instead of <b>BandId</b> to select a band, set <b>BandId</b> = (ULONG) –1.</p>
</dd>

### -field <b>BandStart</b>

<dd>
<p>The starting byte location on the storage device to begin a band search. An attempt is made to match a band at or after <b>BandStart</b>.</p>
</dd>

### -field <b>AuthKeyOffset</b>

<dd>
<p>The offset, in bytes, of an  <b> AUTH_KEY</b> structure containing the authorization key for the band. The offset is from the beginning of <b>DELETE_BAND_PARAMETERS</b>. <b>AUTH_KEY</b> is declared in <i>ehstorbandmgmt.h</i> as the following.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _AUTH_KEY
{
    ULONG   KeySize;
    UCHAR   Key[ANYSIZE_ARRAY];
} AUTH_KEY;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="KeySize"></a><a id="keysize"></a><a id="KEYSIZE"></a>KeySize

<dd>
<p>The size of the key, in bytes, of the key data at <b>Key</b>. If <b>KeySize</b> is set to 0, a default key is used.</p>
</dd>

### -field <a id="Key"></a><a id="key"></a><a id="KEY"></a>Key

<dd>
<p>A variable-length byte array containing the key data.</p>
</dd>
</dl>
<p>To specify a default authentication key to the band, set   <b>AuthKeyOffset</b> = <b>EHSTOR_BANDMGR_NO_KEY</b>. If <b>Flags</b> contains <b>DELBAND_ERASE_BEFORE_DELETE</b>, <b>AuthKeyOffset</b> must be set to <b>EHSTOR_BANDMGR_NO_KEY</b>.</p>
</dd>
</dl>

## -remarks
<p> Precedence is given to <b>BandID</b> for band selection. If <b>BandID</b>  is greater than   0 and  <b>BandID</b>  is less than the  <b>MaxBandCount</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/hh439563">BAND_MANAGEMENT_CAPABILITIES</a>, then   <b>BandID</b> is used as the only selection criteria for a band match. If  <b>BandID</b> == –1, then <b>BandStart</b> is used as  the match criteria to select a band. If no band matches either selection criteria, then STATUS_INVALID_PARAMETER is returned in the <i>IoStatus</i> block for <a href="https://msdn.microsoft.com/library/windows/hardware/hh451376">IOCTL_EHSTOR_BANDMGMT_DELETE_BAND</a>.</p>

<p>If <b>DELBAND_ERASE_BEFORE_DELETE</b> is set in <b>Flags</b>, then an authentication key is not needed to delete the band. If this flag is not set, the current authentication key must be included at <b>AuthKeyOffset</b>.</p>

<p>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439563">BAND_MANAGEMENT_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451376">IOCTL_EHSTOR_BANDMGMT_DELETE_BAND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451383">IOCTL_EHSTOR_BANDMGMT_ERASE_BAND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DELETE_BAND_PARAMETERS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
