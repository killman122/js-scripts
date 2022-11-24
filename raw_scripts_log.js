let logs=[
'%2C%22random%22%3A%2252672211%22%2C%22log%22%3A%221646730319330~1YkglMyG3oIMDF6Q05BYjAyMQ%3D%3D.S3V6d1VJc3x5U0xyej8VMSR3dAM5cSAZHEtveG1UVnIwcxxLPTgDPRIxLBNRNikCACADJjstCAt7fAcVBA%3D%3D.011bd967~6%2C1~117A15E09E719447BF5CC7254753266A8DDB0F31~03cv7yx~C~TBBFWhMPbBNcAR8Fex1wfh19D3wdBh8FBwEUQxBsGxNBWVwaDWkTUwQYAgUUdQQdYwh%2FGwAWBwIBG0UXGxNcAB8EBR13dh1sdX8dBh8FBwEUQxAdFVUEGgQMG3AHG2V2bR1NG0YTah0XUENWFQgAGxNGRBMCFQMHAwcCBAEKDwEGBAECAgYOFR4TQFRRFQsaQ0ZFQ0VTQlcaGxBGUlAXDRNeUUZFQ0VAVhMUFUJVWRMPbAUUAQsIGwgZBgEUBh4Eah0XXVsaDQMdFVJGFQsaVAsCUQJUVlcAB1NVDgQHVlBcUVBVBlMEA1UIAwAADlcXGxNWRxALFX1cWURAF1NDWkcNWxMUFUYTDQADAwcPBAICBggGBAEUFVhaFQsXGlcMUwQDBwVWVQQMBh9XDglXBQUBDwAFAlcCAQheGgECAFMDAgNcBAEDA1cMVVBbBgJSD1RXBlRbVgAHVAlWDwMJVQcTGxNTR1MaDRBHdW5dRVNqBH5be3B3TlRNW1hADwNzQBMUFVxHFQsXcF5XUF5UF3hbVB8aGxBfVkcXDRMBBQsDBRMZFUJbRRALbAYNBx0LAQJsGxNHWBMCbBBhdHB4BwEaGxBQWVVHWFhcFR4TBgEXGxMJBxwFGQIXGxMBBQsDBRMZFQcODgEJBAMDBQIMBAsCDwIYBQIMBAcCAQcCBAcLDgEHARMZFQAaah4TXl5UFQsaUVRXUVdTQ0UaGxBQXRMPFUQaGxBSXhMPFUYLGQAfAxMZFVJeaEQTDRMFBRMUFVBVFQsXRVBWU11cCgQHAQYKBQMAFR0XWlsaDWkCGwAZBmwUFVBdWFYXDRMJAQYHAAIFBQYJAAAESQBRDndVfWV%2FdlZMBgEMU1ZVAVNWBAkNAwBTAVUGD1MLVAZSAgEBUQEBAwZPTh0ESU9GdUxiZXt3clYMZmQABlJ9YWN7b2QFU2RzbVNtcUZjZnMAc2BURGN2dXNkcmBXZHdzRGNgX3B3cmR0YHldfWBuWkZ0cVZSY3BPdmF5X2d9ckZfYHNWVHZ3T3hecl4AdndSUGV5T0VwcnNGZWl9fmVyZXttYmd2ZndZUGBjBkJsdGB7Y3BnXHNwQHNmY1YICk8IBEdJWQQBFR0aWkFWFQsXFUw%3D~0s2p1jb%22%2C%22sceneid%22%3A%22JLHBhPageh5%22%7D',
'%2C%22random%22%3A%2212905311%22%2C%22log%22%3A%221646812348308~1HtKjlR4ihdMDFQU1VMRzAyMQ%3D%3D.YWVhen9hYWZ4cWJmZjIWOmU7BHM0NGckOWF%2FY2BxfGIrfjlhLScgFxIFMH42FTY%2FBGxjHz1%2BaBYLP3QWbW4r.0edfd9b5~6%2C1~A290EE1F3E05BF47591A52E4915064471AFA9C3D~0sl012v~C~SBFGWBEPa2kYEUdcWBEPaxZQBh4GBB9xfxgFf3YeBB0FAAQYRxEeF1cCHQAFH3d9GQJ6AhgFHQMCBR9BEhgWVwIfAQEZdGQYAmNjGUYZRBZpHxFVR10XCgUYEUBBFwkXAQIABQsDBwABCAMGCgUBAwAXHBZDVlcQDxFBREBAR1VHUxEZEkNRUhEIF1VTREBAR0ZTFx8XQFBaEQlpAR8DCQEYCh8DBR8EHAFpHxFYXxEPARgWUEAQDxFWCQdSAFJTUwsFUVANBgFTVFdTUlAFUQIGUQMBAgUNVREeF11FEg4Wf1pcQEsVUVVGUFsEAREZEkAWCQIEAQUNAQYHBwsBBQsZEl5fEQkQGFUBVAIGAwdRVwYBARlRUlEABFcCAFJXAgICUFUEHVIMBQIDDAUFVAcAClZTUQsEU1EMBAQEBFdUAwwMBANUDQcNAFUWHxFURVEXChZGX2NwY1YHQXFRWXsZBn9dAhtya1kKZA4IEhgWXUUQDxFyX1tTX1YSfF1WHhYYEV1TQxEPEg0GCgEAFx8XQ1dGEQlpAgsFHAcCA24eF0FaEg5vEX19ZR50fgQEER8QVF1RQltdVxEeFwIFEhgWAgMcAR0GEhgWCgELBwEXHBYBBQIEBwUHAwUHBwUFBgMGHQICAAUDBgIGAAcBBQUEBAAXHBYFEW4eF1paURYOEVVUU1VTVkBAER8QVFkXChZBER8QVloXChZDAB0AGwcXHBZXVWxEFwkXAAYWHxFQUREPEkZVXVddWA4EAg0EBgADBBEZElleEQlpBB8FHARpHxFQWVxSEg4WAgUGAwsEAgcAAQoGA00EZQMNdANXckMMfnlwdWZrB2VzYmB1S35VCA4bamJiYVABBF9gZm4HV3RKZ2ZPQ1dWcGVRfnt4fX1mRGt9THlleAZYRVZ0fFFWSkBYe2ICTFJdCF99AERVb1tsenpeemJ2ZnZbeXNQZ2dcQmBvYVcGUVlnX3lfAU5%2BcHpeZUoBdFZydmd7bWptdF5XVHB6Rl5gWG5Fe2FjQX5nYV1%2BcGJjfWFBeXFTA2F2UlxjdXdXWHZFAX14SG16eGJ7eGNNeQdye1tCfWIIDRoMAwNWUARUAUpOHwJMS013TmBmaXdgUgNhZwVEaXRkc3RtcQRucl97eGZ0AWBmWwtnZ2UBUXNmaWR0QgdnYlxAcWVncHlndldje2ZoYGUHVHByVANqd3J%2Fd3MEdXBjZF9wcnUEdWZaYFdyXExzdWIKYnIFV3xlYUNwbVtsZXBcfWZwUnZ%2FdkxTZWVeBWFtWGF1cWYCd2B0YWNgcg4PSwNEAEQHXVUQGRFYQ1MWCREQSA%3D%3D~1yaiw5q%22%2C%22sceneid%22%3A%22JLHBhPageh5%22%7D',
'%2C%22random%22%3A%2271106311%22%2C%22log%22%3A%221646812543050~1HHqzPE3LYiMDFxZXJoaDAyMQ%3D%3D.QFNGXlBAV0dbUEdRQBYiJx0XBQAFKRdRFkBJREReXVQMWhZAGwAEODMzF1oZNAAYIENCKRpaRzc9GFA5TFgM.bc9fcc5a~6%2C1~183EA55B9F5F7FC8DFD0B3544C704AA1E37843AF~0wwbuh6~C~SRJHXxYJbhZdBB0HZBh3ZBgIcWUfAxoDBQQVRhJuHhZHW1kbCGsRVgEeAWUVdmMfAXsCGQUXAgADHkARGRZdBR0HYxh3ZhgKYX8fAxoDBQQVRhIfEFACGABrHnRgHgdmfRhMHkQRbxgRUkZXEAoCHhZARhYDEAEFBgILBAYMBgAECgICBAwAEBwRRVFXFw4bRkRHRkBVQFIbHhJEV1URDxZfVERHRkBGVBYVEEBXXBYJbgAVBAkGHg0fBAQVAxwGbxgRX14bCAEfEFdAFw4bUQkAVAdSVFIBAlFXCwEBVFVdVFJXA1YCAVAJBgICC1IRGRZXQhIJEHhaW0FBElFSQFdbAwAbHhJHEA4CAwAPCgEBBwAABQEJHhJZWRYJFxlfBlQFAAQHVlYMBgEeV1VRBwVdBQBVUQUCBVFfAx1VCgICBA0PAlQABg1WVFABA1NWCgMEAwVdUwMLCgMDUwwNCgBSEBgRU0RbEAoRQFhjd2JcAEF2V157Hgd1WgIcdGxZDWUEDxIfEFpFFw4bdV9cVVhWFX1XUR4RHhZdVEIbCBIKAA0BBxYVEENQQBYJbgMBAhwABARuGRZLXRIJaRZ9emQUc34DAhYfF1VXVkJcW1ARGRYIAhIfEAUDGwAXARIfEA0BDAYLEBwRBwICAwYPAAMCAQAFAgcJAR0FBAcFBAcIAQAABwIFAwUKEBwRAxZuGRZQXVERCBZVU1JfVFZHRhYfF1VTEAoRRxYfF1dQEAoRRQcdBxoNEBwRUVJsQxYDEAABEBgRV1AbCBJBU1pXWlkEBQECAgIABAUbHhJeWBYJbgYVAxwCbxgRV1hWVRIJEAUFAQIBAwIGAQAEBQNHAwlYVV9EZFZxekF%2BdnJmbAZvdGJnc0x%2BUgkEHGplZGZQBgVVZ2ZpAVB0TWZsSENQUHdlVn9xf316YENrek1zYngBXkJWc31bUUpHXnxiBU1YWghYewdEUm5Ra3p9WH1icWd8XHl0VmBnW0NqaGFQAFZZYF5zWAFJeHd6WWRABnRRdHFnfGxganRZUVNwfUdUZ1hpQ3xhZEB0YGFaeHdiZHxrRnl2VQRhcVNWZHVwUV92QgB3f0hqfH9ifHlpSnkAdHxbRXxoDw0dCgQDUVEOUwFNSxgCS0pHcE5gcHpycHVeZWVlA1F7WWJ9amZAV2FlUVJsdEBrY1xLfWVvBmF7WnZlcHVeYHVbAmBmZ3Vyd1x6YXxLe2ZvXwFxd2VAZHVef2d7WnZ7cFNKZnJUZ3VxTXFad2Zbc3FUUmJ4SgBwd3YHYmwJe2JwWnlxdENwcHVbCmdmc1NocVhxZ3VxDXVxc3FkZkMOCEoIWwhDA1IEFxgbX0NUEA4RF0k%3D~0hh2iyo%22%2C%22sceneid%22%3A%22JLHBhPageh5%22%7D',
    ]

if (process.env.logs) {
if (process.env.logs.indexOf('\n') > -1) {
    
    logs = process.env.logs.split('\n');
  } else {
    logs = process.env.logs.split();
  }
}
for (let i = 0; i < logs.length; i++) {
  const index = (i + 1 === 1) ? '' : (i + 1);
  exports['logs' + index] = logs[i];
}