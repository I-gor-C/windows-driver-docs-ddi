---
UID : NF:ntstrsafe.RtlStringCbCatNExA
title : RtlStringCbCatNExA function
author : windows-driver-content
description : The RtlStringCbCatNExW and RtlStringCbCatNExA functions concatenate two byte-counted strings while limiting the size of the appended string.
old-location : kernel\rtlstringcbcatnex.htm
old-project : kernel
ms.assetid : 76842444-e733-4dee-b83b-db4ef22f697e
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlStringCbCatNExA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntstrsafe.h
req.include-header : Ntstrsafe.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows XP with Service Pack 1 (SP1) and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RtlStringCbCatNExW,RtlStringCbCatNExA,RtlStringCbCatNExW
req.alt-loc : Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance : 
req.unicode-ansi : RtlStringCbCatNExW (Unicode) and RtlStringCbCatNExA (ANSI)
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ntstrsafe.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PBATTERY_REPORTING_SCALE, BATTERY_REPORTING_SCALE"
---


# RtlStringCbCatNExA function
The <b>RtlStringCbCatNExW</b> and <b>RtlStringCbCatNExA</b> functions concatenate two byte-counted strings while limiting the size of the appended string.

## Syntax

````
NTSTATUS RtlStringCbCatNExW(
  _Inout_opt_ LPTSTR  pszDest,
  _In_        size_t  cbDest,
  _In_opt_    LPCTSTR pszSrc,
  _In_        size_t  cbMaxAppend,
  _Out_opt_   LPTSTR  *ppszDestEnd,
  _Out_opt_   size_t  *pcbRemaining,
  _In_        DWORD   dwFlags
);
````

## Parameters

`pszDest`

A pointer to a buffer which, on input, contains a null-terminated string to which <i>pszSrc</i> will be concatenated. On output, this is the destination buffer that contains the entire resultant string. The string at <i>pszSrc</i>, up to <i>cbMaxAppend</i> bytes, is added to the end of the string at <i>pszDest</i>, and terminated with a null character. The <i>pszDest</i> pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.

`cbDest`

The size of the destination buffer, in bytes. The buffer must be large enough to include both strings and the terminating null character.

For Unicode strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(WCHAR). 

For ANSI strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(char). 

If <i>pszDest</i> is <b>NULL</b>, <i>cbDest</i> must be zero.

`pszSrc`

A pointer to a null-terminated string. This string will be concatenated to the end of the string that is contained in the buffer at <i>pszDest</i>. The <i>pszSrc</i> pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.

`cbToAppend`



`ppszDestEnd`

If the caller supplies a non-<b>NULL</b> address pointer, then after the concatenation operation completes, the function loads that address with a pointer to the destination buffer's resulting <b>NULL</b> string terminator.

`pcbRemaining`

If the caller supplies a non-<b>NULL</b> address pointer, the function loads the address with the number of unused bytes that are in the buffer pointed to by <i>pszDest</i>, including bytes used for the terminating null character.

`dwFlags`

One or more flags and, optionally, a fill byte. The flags are defined as follows: 

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>


## Return Value

The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>This <i>success</i> status means source data was present, the strings were fully concatenated without truncation, and the resultant destination buffer is null-terminated.
<dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl>This <i>warning</i> status means the copy operation did not complete due to insufficient space in the destination buffer. If STRSAFE_NO_TRUNCATION is set in <i>dwFlags</i>, the destination buffer is not modified. If the flag is not set, the destination buffer contains a truncated version of the concatenated string.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.

The function returns the STATUS_INVALID_PARAMETER value when:

## Remarks

<b>RtlStringCbCatNExW</b> and <b>RtlStringCbCatNExA</b> should be used instead of the following functions: 

<b>strncat</b>

<b>wcsncat</b>

The size, in bytes, of the destination buffer is provided to <b>RtlStringCbCatNExW</b> and <b>RtlStringCbCatNExA</b> to ensure that they do not write past the end of the buffer. 

<b>RtlStringCbCatNEx</b> adds to the functionality of <a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatnw.md">RtlStringCbCatN</a> by returning a pointer to the end of the destination string as well as the number of bytes left unused in that string. Flags can be passed to the function for additional control.

Use <b>RtlStringCbCatNExW</b> to handle Unicode strings and  <b>RtlStringCbCatNExA</b> to handle ANSI strings. The form you use depends on your data, as shown in the following table.

WCHAR

L"string"

<b>RtlStringCbCatNExW</b>

<b>char</b>

"string"

<b>RtlStringCbCatNExA</b>

If <i>pszSrc</i> and <i>pszDest</i> point to overlapping strings, the behavior of the function is undefined.

Neither <i>pszSrc</i> nor <i>pszDest</i> can be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set, in which case either or both can be <b>NULL</b>. If <i>pszDest</i> is <b>NULL</b>, <i>pszSrc</i> must either be <b>NULL</b> or point to an empty string.

For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntstrsafe.h (include Ntstrsafe.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatexw.md">RtlStringCbCatEx</a>
</dt>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcbcatnw.md">RtlStringCbCatN</a>
</dt>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcchcatnexw.md">RtlStringCchCatNEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCbCatNExW function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>