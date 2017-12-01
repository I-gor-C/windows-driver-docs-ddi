---
UID: NF.wudfddi.IWDFNamedPropertyStore.GetNamedValue
title: IWDFNamedPropertyStore::GetNamedValue
author: windows-driver-content
description: The GetNamedValue method retrieves the value of a property.
old-location: wdf\iwdfnamedpropertystore_getnamedvalue.htm
old-project: wdf
ms.assetid: 9581e3af-f7f8-4365-8bb2-daedcb7a3280
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IWDFNamedPropertyStore, GetNamedValue, IWDFNamedPropertyStore::GetNamedValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFNamedPropertyStore.GetNamedValue
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFNamedPropertyStore
req.product: Windows 10 or later.
---

# IWDFNamedPropertyStore::GetNamedValue method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>GetNamedValue</b> method retrieves the value of a property.</p>


## -syntax

````
HRESULT GetNamedValue(
  [in]  LPCWSTR     pszName,
  [out] PROPVARIANT *pv
);
````


## -parameters
<dl>

### -param <i>pszName</i> [in]

<dd>
<p>A pointer to a null-terminated string that contains the name of the property.</p>
</dd>

### -param <i>pv</i> [out]

<dd>
<p>A pointer to a variable that receives the value for the property. </p>
</dd>
</dl>

## -returns
<p><b>GetNamedValue</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The <b>GetNamedValue</b> method allocates memory for a string in the <a href="stg.propvariant">PROPVARIANT</a> structure pointed to by the <i>pv</i> parameter.   The caller must then free this memory by calling the <a href="stg.propvariantclear">PropVariantClear</a> function, as shown in the following snippet:</p>

<p>If the caller does not free the memory, a memory leak may result.</p>

<p>The following variant types are supported for property values. The following table shows the variant type that is returned regardless of the original variant type.</p>

<p>VT_BSTR</p>

<p>While clients read a string value, the value is returned as VT_LPWSTR regardless of the original variant type that was used to write the value.</p>

<p>VT_LPWSTR</p>

<p>VT_LPSTR</p>

<p>VT_I1</p>

<p>While clients read an integer value, the value is returned as VT_UI4 regardless of the original variant type that was used to write the value.</p>

<p>VT_UI1</p>

<p>VT_I2</p>

<p>VT_UI2</p>

<p>VT_I4</p>

<p>VT_UI4</p>

<p>VT_UINT</p>

<p>VT_BLOB</p>

<p>The binary value is returned as VT_BLOB.</p>

<p>VT_VECTOR | VT_LPWSTR</p>

<p>The string array is returned as VT_VECTOR | VT_LPWSTR</p>

<p>A string that contains environment variables is expanded on read.</p>

<p>For more information, see <a href="wdf.using_the_registry_in_umdf_drivers">Using the Registry in UMDF-based Drivers</a>.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfnamedpropertystore.md">IWDFNamedPropertyStore</a>
</dt>
<dt>
<a href="stg.propvariantclear">PropVariantClear</a>
</dt>
<dt>
<a href="stg.propvariant">PROPVARIANT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFNamedPropertyStore::GetNamedValue method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
